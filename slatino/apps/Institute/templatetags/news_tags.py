from django import template
from slatino.apps.Institute.models import Institute
register = template.Library()


@register.inclusion_tag('Institute/box_news.html')
def pull_latest_institute(howmany=50):
    all_institute = Institute.objects.all()
    return dict(all_institute=all_institute)


@register.inclusion_tag('Institute/incontent_news.html')
def incontent_latest_institute(howmany=50):
    all_institute = Institute.objects.all()
    return dict(all_institute=all_institute)
