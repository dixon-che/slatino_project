from django import template
from slatino.apps.Links.models import Links
register = template.Library()

@register.inclusion_tag('Links/box_links.html')
def pull_latest_links(howmany=5):
    all_links = Links.objects.all().order_by('-pub_date')[:howmany]
    return dict(all_links=all_links)

@register.inclusion_tag('Links/incontent_links.html')
def incontent_latest_links(howmany=5):
    all_links = Links.objects.all().order_by('-pub_date')[:howmany]
    return dict(all_links=all_links)
