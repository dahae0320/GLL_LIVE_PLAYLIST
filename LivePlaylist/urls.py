from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_playlist/', views.make_playlist, name='make_playlist'),
    path('make_playlist/playlist/<int:playlist_id>', views.playlist, name='playlist'),
    path('search_result/', views.search_result, name='search_result'),
    path('load_playlist/', views.load_playlist, name='load_playlist'),
]
