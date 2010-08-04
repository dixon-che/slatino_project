from django import template
from dcdjutils.Articles.models import Article
register = template.Library()

@register.inclusion_tag('Articles/box.html')
def pull_latest_articles(howmany=5):
    articles = Article.objects.filter(published=True).order_by('-pub_date')[:howmany]
    return dict(articles=articles)

@register.inclusion_tag('Articles/incontent.html')
def incontent_latest_articles(howmany=5):
    articles = Article.objects.filter(published=True).order_by('-pub_date')[:howmany]
    return dict(articles=articles)
