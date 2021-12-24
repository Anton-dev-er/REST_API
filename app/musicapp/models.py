from django.db import models as m
from slugify import slugify


class Singer(m.Model):
    nickname = m.CharField(max_length=255, unique=True)
    first_name = m.CharField(max_length=255)
    last_name = m.CharField(max_length=250)
    image = m.ImageField(upload_to="photos/singer/%m/%d/", null=True, blank=True)

    slug = m.SlugField(max_length=255, unique=True, blank=True)

    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        super(Singer, self).save(*args, **kwargs)

    def __str__(self):
        return self.nickname


class Song(m.Model):
    name = m.CharField(max_length=255)
    singer = m.ManyToManyField('Singer', related_name='singers')
    release_date = m.DateTimeField()

    slug = m.SlugField(max_length=255, unique=True, blank=True)

    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        print(self.slug, str(self.name))
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
