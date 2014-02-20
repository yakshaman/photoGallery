from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'photoGallery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('photos.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
