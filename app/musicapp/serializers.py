from rest_framework import serializers

from .models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=Singer.objects.all(),
        slug_field='nickname'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='song-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Song
        fields = ['url', 'id', 'name', 'release_date', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='singer-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Singer
        fields = ['url', 'id', 'nickname', 'first_name', 'last_name', 'image']


class SingerAddForSong(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='singer-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Singer
        fields = ['url', 'id', 'nickname']
