from django.conf.urls.defaults import *
from slatino.Gallery.models import Item, Photo
from django.conf import settings


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('django.views.generic',
    url(r'^$', 'list_detail.object_list',
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'Gallery/items_list.html',
            'allow_empty': True
        },
        name='item_list'
    ),
    url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
        kwargs={
            'queryset': Item.objects.all(),
            'template_name': 'Gallery/items_detail.html'
        },
        name='item_detail'
    ),
    url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail', 
        kwargs={
            'queryset': Photo.objects.all(),
            'template_name': 'Gallery/photos_detail.html'
        },
        name='photo_detail'
    ),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
	)
