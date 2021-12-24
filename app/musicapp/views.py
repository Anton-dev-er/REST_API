from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics

from django.http import Http404

from .models import Song, Singer
from .serializers import *


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
