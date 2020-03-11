from django.contrib import admin
from music.models import Album, Track, Artist

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)