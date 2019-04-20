from json import JSONEncoder
from django.http import JsonResponse
from .models import Track
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print(request.POST)
    query_music = Track.objects.order_by('?').first()
    album_title = query_music.album.title
    query_music = 'http://127.0.0.1:8000/media/{}'.format(str(query_music.music))
    context = {}
    track = {}
    album = {}
    context['status'] = 'ok'
    context['message'] = album
    album['Album'] = album_title
    album['Track'] = track
    track['path'] = query_music
    return JsonResponse(context, encoder=JSONEncoder, safe=False)
