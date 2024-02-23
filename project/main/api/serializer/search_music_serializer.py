from rest_framework import serializers


class CommonErrorResponseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    details = serializers.CharField()


class SearchMusicSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    audio = serializers.FileField(required=True, format='mp3')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    # def validate_image(self, value: InMemoryUploadedFile):
    #     if value.size > 2 * 1024 * 1024:
    #         raise serializers.ValidationError("image size should be less than 2M !")
    #     return value
    #
    # def validate_content(self, value):
    #     without_html_tag_len = CommonsUtils.calculate_text_length_without_htmltag(value)
    #     if without_html_tag_len > 2000 or without_html_tag_len < 3:
    #         raise serializers.ValidationError("large text!")
    #     return value


class SearchMusicResponseSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    msg = serializers.CharField()
