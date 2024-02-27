# import typing
#
# import os
#
# from typing import List, Dict
#
# from project.main.utils.base_config import CommonsBaseConfig
#
#
# class Configuration:
#     _config_class = CommonsBaseConfig
#
#     DOCKER_SECRET_DEFAULT_LOCATION = "/run/secrets/"
#
#     @classmethod
#     def find_dotenv(cls, filename: str, alternative_env_search_dir: str):
#
#         from dotenv import load_dotenv, find_dotenv, dotenv_values
#         file_path = ""
#         try:
#             file_path = find_dotenv(filename=filename)
#         except:
#             print("Warning: First try to find .env file failed!")
#         if len(file_path) == 0 and alternative_env_search_dir is not None:
#             for dirname in CommonsUtils.walk_all_parent_dirs(alternative_env_search_dir):
#                 check_path = os.path.join(dirname, filename)
#                 if os.path.isfile(check_path):
#                     return check_path
#
#         return file_path
#
#     @classmethod
#     def configure(cls, cls_type: type, is_test=False,
#                   alternative_env_search_dir: str = None, silent: bool = False):
#         """
#         Configure project specific configuration for commons lib
#         @param cls_type:  Project specific configuration(e.g.  child of .. py:class:: ncl.utils.config.base_config.CommonsBaseConfig)
#         @param is_test:
#         @param alternative_env_search_dir:
#         """
#
#         cls._config_class = cls_type
#
#         if alternative_env_search_dir is None and not silent:
#             print(
#                 "Warning: alternative_env_search_dir is set to None. .env files can not be found when venv dir located"
#                 "\noutside of project main directory. you can use alternative_env_search_dir=__file__ to avoid it."
#                 "\n use silent = True to suppress this warning")
#         filename = '.env'
#         if is_test:
#             filename = '.env.test'
#
#         from dotenv import load_dotenv, dotenv_values
#         dotenv_values = dotenv_values(
#             cls.find_dotenv(filename=filename, alternative_env_search_dir=alternative_env_search_dir))
#
#         all_annotated_fields = cls.get_all_annotated_fields(cls._config_class)
#
#         for env_attr in dotenv_values:
#             if not hasattr(cls._config_class, env_attr):
#                 # set .env field to class to replace with env values in next loop
#                 setattr(cls._config_class, env_attr, None)
#         load_dotenv(cls.find_dotenv(filename=filename, alternative_env_search_dir=alternative_env_search_dir))
#         for attr_name in dir(cls._config_class):
#             if attr_name.startswith("__") or callable(getattr(cls._config_class, attr_name)):
#                 continue
#
#             read_value = cls.read_from_docker_secret(attr_name)
#
#             if read_value is None:
#                 read_value = os.getenv(attr_name)
#                 if read_value is None:
#                     continue
#
#             annotated_type = all_annotated_fields.get(attr_name)
#
#             try:
#                 final_value = cls.set_value_for_class(cls._config_class, attr_name, read_value, annotated_type)
#                 setattr(cls._config_class, attr_name, final_value)
#
#             except:
#                 raise DefinitionException(
#                     "Configuration field format Exception: For field {} got {}  expected {}.".format(attr_name, str(
#                         annotated_type), read_value))
#
#
#     @classmethod
#     def config(cls):
#         return cls._config_class
#
#     @classmethod
#     def read_from_docker_secret(cls, attr_name: str):
#         data = None
#         try:
#             with open(cls.DOCKER_SECRET_DEFAULT_LOCATION + attr_name, 'r') as file:
#                 data = file.read().rstrip()
#         except:
#             pass
#         return data
#
#     @classmethod
#     def set_value_for_class(cls, clazz, attr_name, env_value: str, annotated_field_class=None):
#         class_value = getattr(clazz, attr_name)
#         if annotated_field_class and not type(annotated_field_class).__name__ == '_GenericAlias':
#             if issubclass(annotated_field_class, str):
#                 return env_value
#         if annotated_field_class:
#             return eval(env_value)
#
#         if class_value:
#             if isinstance(class_value, str):
#                 return env_value
#             return eval(env_value)
#         return env_value
#
#
# if __name__ == '__main__':
#     from dotenv import load_dotenv, dotenv_values, find_dotenv
#
#     ll = List
#     d = KafkaBaseConfig()
#     # print(issubclass(d.__annotations__["KAFKA_BROKERS_LIST"],List))
#     bb = d.__annotations__["KAFKA_BROKERS_LIST"]
#     print(dir(type(bb)))
#
#
#     class s(CommonsBaseConfig):
#         KAFKA_BROKERS_LIST = []
#         ff: dict = None
#         pass
#
#
#     Configuration.configure(s)
