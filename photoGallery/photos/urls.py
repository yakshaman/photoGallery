from django.conf.urls import patterns, url

from photos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^album/$', views.index, name='index'),
    url(r'^photo/$', views.index, name='index'),
    url(r'^album/(?P<album_id>\d+)/$', views.album, name='album'),
    url(r'^photo/(?P<photo_id>\d+)/$', views.photo, name='photo'),
)