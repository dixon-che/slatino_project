from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.http import Http404, HttpResponse, HttpResponseRedirect

from slatino.Publications.models import Publication, PublicationPhoto

publication_last_count = settings.PUBLICATION_LAST_COUNT or 5
publication_per_page = settings.PUBLICATION_PER_PAGE or 10


def publication_last(request, post_type=None):
    if post_type is None:
        publications = Publication.objects.filter(published=True).order_by('order').order_by('-pub_date')[:publication_last_count]
        return render_to_response("Publications/list.html", RequestContext(request,
                              dict(publications=publications, title=_(u'Last information'))))
    else:
        publications = Publication.objects.filter(published=True, post_type=post_type).order_by('order').order_by('-pub_date')[:publication_last_count]
        return render_to_response("Publications/list.html", RequestContext(request,
                              dict(publications=publications, title=_(u'Last %s') % post_type)))


def publication_list(request, post_type):
    publications = Publication.objects.filter(published=True, post_type=post_type).order_by('order').order_by('-pub_date')
    page = request.GET.get('page', None)

    if page is not None:
        if page.isdigit():
            page = int(page)
        else:
            raise Http404
        publications = publications[page*publication_per_page:page*publication_per_page+publication_per_page]
    else:
        publications = publications[:publication_per_page]

    if not publications:
        raise Http404

    return render_to_response("Publications/list.html", RequestContext(request,
                              dict(publications=publications, title=_(u'List '+post_type))))


def publication_view(request, publication_slug):
    publication = get_object_or_404(Publication, slug=publication_slug)
    return render_to_response("Publications/one.html", RequestContext(request,
                              dict(publication=publication)))


def past_image(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id, post_type='article')
    return render_to_response("Publications/past_image.html", RequestContext(request, dict(publication=publication)))


def image_view(request, image_id, size=None):
    image = get_object_or_404(PublicationPhoto, id=image_id)

    if size is None:
        return  HttpResponseRedirect(image.image.url)

    return  HttpResponseRedirect(image.thumbnail_url(size))
