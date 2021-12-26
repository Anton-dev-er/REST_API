from django.urls import path

from .views import *

urlpatterns = [
    path("song/", SongListView.as_view(), name='song-list'),
    path("song/detail/<slug:slug>", SongDetailView.as_view(), name='song-detail'),
    path("song/add", SongAddView.as_view(), name='song-add'),

    path("singer/", SingerListView.as_view(), name='singer-list'),
    path("singer/detail/<slug:slug>", SingerDetailView.as_view(), name='singer-detail'),
    path("singer/add", SingerAddView.as_view(), name='singer-add'),

    path("", api_root),
]