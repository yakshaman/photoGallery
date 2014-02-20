from django.shortcuts import render
from django.template import RequestContext, loader

from photos.models import Album
# Create your views here.

from django.http import HttpResponse

def index(request):
    album_list = Album.objects.order_by('date')
    template = loader.get_template('photos/index.html')
    context = RequestContext(request, {'album_list' : album_list,})
    return HttpResponse(template.render(context))

def album(request, album_id):
    return HttpResponse("here should go da photo list for album %s" % str(album_id))

def photo(request, photo_id):
    return HttpResponse("here should go da photo %s" % str(photo_id))
