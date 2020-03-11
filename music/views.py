from django.shortcuts import render
from .models import Album, Track
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

class AlbumCreateView(CreateView):
    model = Album
    fields = ['album_name','year','description']


class AlbumListView(ListView):
    model = Album
    context_object_name = 'albums'

class AlbumDetailView(DetailView):
    model = Album
    

class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['album_name','year','description']

class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/'

class TrackListView(ListView):
    model = Track
    context_object_name = 'tracks'


