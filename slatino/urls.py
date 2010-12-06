import os
from django.conf.urls.defaults import *
from settings import *
from django.shortcuts import render_to_response, get_object_or_404
from registration.forms import RegistrationFormUniqueEmail
from forms import CustomRegistration
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "slatino.views.index"),
    (r'^robots\.txt$', "slatino.views.robots"),
    (r'^news/', include('slatino.News.urls')),
    (r'^article/', include('slatino.Articles.urls')),
    #(r'^links/', include('slatino.Links.urls')),
    (r'^gallery/', include('slatino.Gallery.urls')),
    (r'^personalee/', include('slatino.Personalee.urls')),
    (r'^institute/', include('slatino.Institute.urls')),
    (r'^telephone/', include('slatino.Telephone.urls')),
    (r'^transport/', include('slatino.Transport.urls')),
    #(r'^i18n/', include('django.conf.urls.i18n')),
    (r'^tag/(?P<slug>\w+)/$', 'slatino.views.tag'),
    (r'^captcha/(?P<code>[\da-f]{32})/$', 'supercaptcha.draw'),
    (r'^accounts/register/$', 'registration.views.register', {'form_class': CustomRegistration, 'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/profile/$', 'slatino.views.index'),
    (r'^profiles/', include('profiles.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
)


if MEDIA_APACHE_DIRECT == False:
    urlpatterns += patterns('',
        (r'^(img/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(css/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(tiny_mce/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(emotions/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(news_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(article_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(gallery_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(institute_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(personalee_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(profile_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(articles-media/.*)$', 'django.views.static.serve', {'document_root': SITE_PATH + "dcdjutils/Articles/"}),
        (r'^tagsfield/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(LIB_PATH, "tagsfield/media/")}),
)
