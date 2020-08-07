from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'LivePlaylist/index.html')

def playlist(request):
    return render(request, 'LivePlaylist/playlist.html')