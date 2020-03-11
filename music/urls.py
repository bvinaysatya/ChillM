from django.urls import path
from music.views import (
    AlbumCreateView,
    AlbumDeleteView,
    AlbumDetailView,
    AlbumListView,
    AlbumUpdateView,
    TrackListView
)

urlpatterns = [
    path('album/new/', AlbumCreateView.as_view(), name="album-create"),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name="album-update"),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name="album-detail"),
    path('', AlbumListView.as_view(), name="album-home"),
    path('album/<int:pk>/delete', AlbumDeleteView.as_view(), name="album-delete"),
    path('album/<int:pk>/delete', TrackListView.as_view(), name="track-list")

]