import os

from project.configuration.base_config import CommonsBaseConfig


class Configuration:
    _config_class = CommonsBaseConfig

    @classmethod
    def all_base_classes(cls, clazz):
        base_class_set = set(clazz.__bases__)
        all_base_class_set = set({clazz})
        all_base_class_set.update(base_class_set)
        for base in base_class_set:
            all_base_class_set.update(cls.all_base_classes(base))
        return all_base_class_set

    @classmethod
    def get_all_annotated_fields(cls, clazz):

        all_base_classes = cls.all_base_classes(clazz)
        all_inherited_fields = dict()
        for base in all_base_classes:
            if hasattr(base, "__annotations__"):
                for key, value in base.__annotations__.items():
                    all_inherited_fields[key] = value

        return all_inherited_fields

    @classmethod
    def configure(
            cls, cls_type: type,
            is_test=False
    ):
        cls._config_class = cls_type

        filename = '.env'
        if is_test:
            filename = '.env.test'

        from dotenv import load_dotenv, dotenv_values, find_dotenv
        dotenv_values = dotenv_values(find_dotenv(filename=filename))

        all_annotated_fields = cls.get_all_annotated_fields(cls._config_class)

        for env_attr in dotenv_values:
            if not hasattr(cls._config_class, env_attr):
                # set .env field to class to replace with env values in next loop
                setattr(cls._config_class, env_attr, None)
        load_dotenv(find_dotenv(filename=filename))
        for attr_name in dir(cls._config_class):
            if attr_name.startswith("__") or callable(getattr(cls._config_class, attr_name)):
                continue

            read_value = os.getenv(attr_name)
            if read_value is None:
                continue

            annotated_type = all_annotated_fields.get(attr_name)

            try:
                final_value = cls.set_value_for_class(cls._config_class, attr_name, read_value, annotated_type)
                setattr(cls._config_class, attr_name, final_value)

            except:
                raise Exception(
                    "Configuration field format Exception: For field {} got {}  expected {}.".format(attr_name, str(
                        annotated_type), read_value))

    @classmethod
    def config(cls):
        return cls._config_class

    @classmethod
    def set_value_for_class(cls, clazz, attr_name, env_value: str, annotated_field_class=None):
        class_value = getattr(clazz, attr_name)
        if annotated_field_class and not type(annotated_field_class).__name__ == '_GenericAlias':
            if issubclass(annotated_field_class, str):
                return env_value
        if annotated_field_class:
            return eval(env_value)

        if class_value:
            if isinstance(class_value, str):
                return env_value
            return eval(env_value)
        return env_value
