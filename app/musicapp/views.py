from django.http import HttpResponseBadRequest
from rest_framework import generics, permissions

from .permissions import IsAuthOrReadOnly
from .serializers import *


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [IsAuthOrReadOnly]

    def perform_create(self, serializer):
        if str(self.request.user) == 'admin':
            print(self.request.user)


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [IsAuthOrReadOnly]

