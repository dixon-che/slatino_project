from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from slatino.News.models import News


def news_list(request):
    all_news = News.objects.all().order_by('-pub_date')
    page = {'title': "All news"}
    return render_to_response("News/list.html",
                              context_instance=RequestContext(request, {"all_news": all_news,
                                                                        "page": page}))


def news_show(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render_to_response("News/one.html",
                              context_instance=RequestContext(request, {"news": news}))


def news_show_spec(request, slug):
    page = {}
    if slug=="last":
        all_news = News.objects.all().order_by('-pub_date')[0:9]
        page['title'] = _("Last news")
    else:
        Http404()
    return render_to_response("News/list.html",
                              context_instance=RequestContext(request, {"all_news": all_news,
                                                                        "page": page}))
