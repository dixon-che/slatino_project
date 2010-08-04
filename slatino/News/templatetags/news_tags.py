from django import template
from slatino.News.models import News
register = template.Library()

@register.inclusion_tag('News/box_news.html')
def pull_latest_news(howmany=5):
    all_news = News.objects.all().order_by('-pub_date')[:howmany]
    return dict(all_news=all_news)

@register.inclusion_tag('News/incontent_news.html')
def incontent_latest_news(howmany=5):
    all_news = News.objects.all().order_by('-pub_date')[:howmany]
    return dict(all_news=all_news)