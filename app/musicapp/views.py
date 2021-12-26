from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404, redirect

from .permissions import IsAuthOrReadOnlyCustom
from .serializers import *


@api_view(['GET'])
def api_root(request):
    return Response({
        'song': reverse('song-list', request=request),
        'singer': reverse('singer-list', request=request),
    })


class SongListView(APIView):
    permission_classes = [IsAuthOrReadOnlyCustom]

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True, context={'request': request})
        return Response(serializer.data)


class SongDetailView(APIView):
    permission_classes = [IsAuthOrReadOnlyCustom]

    def get(self, request, slug):
        song = get_object_or_404(Song, slug=slug)
        serializer = SongSerializer(song, context={'request': request})
        return Response(serializer.data)

    def put(self, request, slug):
        song = get_object_or_404(Song, slug=slug)
        serializer = SongSerializer(song, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        get_object_or_404(Song, slug=slug).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongAddView(APIView):
    def get(self, request):
        singers = Singer.objects.all()
        serializer = SingerAddForSong(singers, many=True, context={'request': request})
        return Response({
            "__Example add song": {
                "name": "",
                "release_date": "2000-01-01T00:00:00Z",
                "singer": [
                    "nickname1",
                    "nickname2",
                    "nickname3"
                ]
            },
            "Singer(s)": serializer.data
        })

    def post(self, request):
        serializer = SongSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingerListView(APIView):
    permission_classes = [IsAuthOrReadOnlyCustom]

    def get(self, request):
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True, context={'request': request})
        return Response(serializer.data)


class SingerDetailView(APIView):
    permission_classes = [IsAuthOrReadOnlyCustom]

    def get(self, request, slug):
        singer = get_object_or_404(Singer, slug=slug)
        serializer = SingerSerializer(singer, context={'request': request})
        return Response(serializer.data)

    def put(self, request, slug):
        singer = get_object_or_404(Singer, slug=slug)
        serializer = SongSerializer(singer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        get_object_or_404(Singer, slug=slug).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SingerAddView(APIView):
    def get(self, request):
        return Response({"Example add singer" :{"nickname": "",
                         "first_name": "",
                         "last_name": ""}})

    def post(self, request):
        serializer = SingerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


