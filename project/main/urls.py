from django.urls import path

from project.main.api.controller.search_music_controller import SearchMusicController

urlpatterns = [
    path(
        'main/search/music',
        SearchMusicController.as_view(),
        name='search-music'
    ),
]
