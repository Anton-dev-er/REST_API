from django.utils.timezone import now
from rest_framework import serializers

from .models import Song, Singer


class SingerSerializerInSong(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='singer-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Singer
        fields = ['url', 'nickname']

    # def get_url(self, obj):
    #     return 'test'


class SongSerializer(serializers.ModelSerializer):
    singer = SingerSerializerInSong(many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='song-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Song
        fields = ['url', 'id', 'name', 'release_date', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        exclude = ['slug', 'created_at', 'updated_at']
