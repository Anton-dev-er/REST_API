from django.urls import path

from .views import *

urlpatterns = [
    path("song/", SongListView.as_view()),
    path("song/<int:pk>", SongDetailView.as_view()),
]