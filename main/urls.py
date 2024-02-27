from django.urls import path

from main.api.controller.search_music_controller import SearchMusicController

urlpatterns = [
    path(
        'main/search/music',
        SearchMusicController.as_view(),
        name='search-music'
    ),
]
