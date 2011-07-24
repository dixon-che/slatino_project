import os
from django.conf.urls.defaults import *
from settings import *
from forms import CustomRegistration
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "slatino.views.index"),
    url(r'^auth/', include('publicauth.urls')),
    (r'^robots\.txt$', "slatino.views.robots"),
    #(r'^news/', include('slatino.News.urls')),
    (r'^publication/', include('slatino.apps.Publications.urls')),
    #(r'^links/', include('slatino.apps.Links.urls')),
    (r'^gallery/', include('slatino.apps.Gallery.urls')),
    (r'^person/', include('slatino.apps.Persons.urls')),
    (r'^institute/', include('slatino.apps.Institute.urls')),
    (r'^telephone/', include('slatino.apps.Telephone.urls')),
    url(r'^transport/raspisanie-avtobusov', 'slatino.apps.Publications.views.publication_view', {'publication_slug': 'raspisanie-avtobusov'}, name='raspisanie-avtobusov'),
    url(r'^transport/raspisanie-elektropoezdov', 'slatino.apps.Publications.views.publication_view', {'publication_slug': 'raspisanie-elektropoezdov'}, name='raspisanie-elektropoezdov'),
    (r'^transport/', include('slatino.apps.Transport.urls')),
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
        #(r'^(news_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(publication_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(gallery_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(institute_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(person_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(profile_images/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(Publication-media/.*)$', 'django.views.static.serve', {'document_root': ROOT_PATH + "apps/Publications/"}),
        (r'^tagsfield/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(LIB_PATH, "tagsfield/media/")}),
        (r'^(jquery-lightbox-0.5/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
        (r'^(widgets/.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
