from django import template
#from dcdjutils.Articles.models import Article
from slatino.Publications.models import Publication
register = template.Library()


@register.inclusion_tag('Publications/box.html')
def pull_latest_publications(post_type, howmany=5):
    publications = Publication.objects.filter(published=True, post_type=post_type).order_by('-pub_date')[:howmany]
    return dict(publications=publications)


@register.inclusion_tag('Publications/incontent.html')
def incontent_latest_publications(howmany=5):
    publications = Publication.objects.filter(published=True, post_type='article').order_by('-pub_date')[:howmany]
    return dict(publications=publications)
