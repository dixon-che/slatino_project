from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.http import Http404, HttpResponse, HttpResponseRedirect

from dcdjutils.Articles.models import Article, ArticlePhoto

article_last_count = settings.ARTICLE_LAST_COUNT or 5
article_per_page = settings.ARTICLE_PER_PAGE or 10

def article_last(request):
    articles = Article.objects.filter(published=True).order_by('order').order_by('-pub_date')[:article_last_count]
    return render_to_response("Articles/list.html", RequestContext(request,
                              dict(articles=articles, title=_(u"Last Articles"))))

def article_list(request):
    articles = Article.objects.filter(published=True).order_by('order').order_by('-pub_date')
    page = request.GET.get('page', None)

    if page is not None:
        if page.isdigit():
            page = int(page)
        else:
            return Http404()
        articles = articles[page*article_per_page:page*article_per_page+article_per_page]
    else:
        articles = articles[:article_per_page]
        
    if not articles:
        return Http404()
        
    return render_to_response("Articles/list.html", RequestContext(request,
                              dict(articles=articles, title=_(u"List Articles"))))
                              
def article_view(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render_to_response("Articles/one.html", RequestContext(request,
                              dict(article=article)))

def past_image(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render_to_response("Articles/past_image.html", RequestContext(request, dict(article=article)))


def image_view(request, image_id, size=None):
    image = get_object_or_404(ArticlePhoto, id=image_id)

    if size is None:
        return  HttpResponseRedirect(image.image.url)
  
    return  HttpResponseRedirect(image.thumbnail_url(size))
