from rest_framework import serializers

from .models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    singer = serializers.SlugRelatedField(slug_field='nickname', many=True, queryset=Singer.objects.all())

    class Meta:
        model = Song
        fields = ['id', 'name', 'release_date', 'singer']
