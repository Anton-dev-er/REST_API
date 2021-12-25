from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, renderers

from .permissions import IsAuthOrReadOnlyCustom
from .serializers import *


@api_view(['GET'])
def api_root(request):
    return Response({
        'song': reverse('song-list', request=request)
    })


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if str(self.request.user) == 'admin':
            print(self.request.user)


class SongDetailView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthOrReadOnlyCustom]


class SingerListView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SingerDetailView(generics.RetrieveUpdateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthOrReadOnlyCustom]


