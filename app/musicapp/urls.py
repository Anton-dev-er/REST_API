from django.urls import path

from .views import *

urlpatterns = [
    path("song/", SongListView.as_view(), name='song-list'),
    path("song/<slug:slug>", SongDetailView.as_view(), name='song-detail'),

    path("singer/", SingerListView.as_view(), name='singer-list'),
    path("singer/<slug:slug>", SingerDetailView.as_view(), name='singer-detail'),

    path("", api_root),
]