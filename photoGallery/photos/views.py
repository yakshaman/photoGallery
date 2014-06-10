from django.shortcuts import render
from django.template import RequestContext, loader

from django.conf import settings

from photos.models import Album
from photos.models import Photo

# Create your views here.

from django.http import HttpResponse

def index(request):
    album_list = Album.objects.order_by('date')
    template = loader.get_template('photos/index.html')
    context = RequestContext(request, {'album_list' : album_list,})
    return HttpResponse(template.render(context))

def album(request, album_id):
    album = Album.objects.get(id=album_id)
    photo_list = Photo.objects.order_by('date').filter(album=album_id)
    template = loader.get_template('photos/album.html')
    context = RequestContext(request, {'photo_list' : photo_list, 'album' : album})
    return HttpResponse(template.render(context))

def photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo.path = settings.STATIC_URL + photo.gen_filename
    photo.path_m = settings.STATIC_URL + "M_" + photo.gen_filename
    photo.path_l = settings.STATIC_URL + "L_" + photo.gen_filename
    template = loader.get_template('photos/photo.html')
    context = RequestContext(request, {'photo' : photo, })
    return HttpResponse(template.render(context))
