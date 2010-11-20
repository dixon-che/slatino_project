from django.conf.urls.defaults import *

urlpatterns = patterns('slatino.Articles.views',
    url(r'^last/$', 'article_last', name='article-last'),
    url(r'^$', 'article_list', name='article-list'),
    url(r'^view/(?P<article_slug>\w+)/$', 'article_view', name='article-view'),
    url(r'^(?P<article_id>\d+)/past_image/$', 'past_image'),
    url(r'^image/(?P<image_id>\d+)/$', 'image_view', name='article-image-view'),
    url(r'^image/(?P<image_id>\d+)/(?P<size>\d+)/$', 'image_view', name='article-image-view-thumb'),
)
