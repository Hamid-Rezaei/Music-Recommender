from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView

from main.api.serializer.search_music_serializer import SearchMusicSerializer, SearchMusicResponseSerializer, \
    CommonErrorResponseSerializer
from main.logic.search_music_logic import SearchMusicLogic


class SearchMusicController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_music_logic = SearchMusicLogic()

    @extend_schema(
        tags=["search_music",],
        request=SearchMusicSerializer,
        summary="Search music by audio",
        operation_id="search_music",
        responses={
            200: SearchMusicResponseSerializer,
            400: CommonErrorResponseSerializer,
            500: CommonErrorResponseSerializer
        }
    )
    def post(self, request):
        try:
            body: dict = request.data
            validation = SearchMusicSerializer(data=body)

            if not validation.is_valid():
                return JsonResponse({"details": 'Bad Request Body.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                res = self.technical_post_logic.create_post(
                    author=request.user,
                    content=validation.validated_data.get("content"),
                    title_list=validation.validated_data.get("title"),
                    image=validation.validated_data.get("image")
                )

                response = {'msg': 'success'}
                serialized_response = SearchMusicResponseSerializer(response)
                return JsonResponse(serialized_response.data, status=status.HTTP_200_OK)

        except Exception as error:
            return JsonResponse({'details': error.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

