import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Playlist,Music

# Create your views here.
def index(request):
    return render(request, 'LivePlaylist/index.html')

def make_playlist(requset):
    playlist = Playlist()
    playlist.save()
    playlist_id = playlist.id
    # print(playlist.id)
    return redirect('playlist/'+str(playlist_id))

def playlist(request, playlist_id):
    return render(request, 'LivePlaylist/playlist.html')

def search_result(request):
    videos = []

    if request.method == 'GET':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.GET['q'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        video_ids = []
        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9,
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        for result in results:
            # print(result['snippet']['title'])
            # print(result['id'])
            # print(parse_duration(result['contentDetails']['duration']))
            # print(result['snippet']['thumbnails']['high']['url'])
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : parse_duration(result['contentDetails']['duration']),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }
    # print(videos[0].get('id'))
    return render(request, 'LivePlaylist/search_result.html', context)

def load_playlist(request):
    if request.is_ajax and request.method == 'POST':
        music = Music()
        music.title = request.POST['video_title']
        music.video_id = request.POST['video_id']
        music.save()
        
        video_data = {
            'video_id' : music.video_id,
            'video_title' : music.title
        }

        return render(request,'LivePlaylist/load_playlist.html', video_data)

    return render(request, 'LivePlaylist/load_playlist.html')