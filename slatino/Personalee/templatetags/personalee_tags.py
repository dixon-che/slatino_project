from django import template
from slatino.Personalee.models import Personalee
register = template.Library()

@register.inclusion_tag('Personalee/box_news.html')
def pull_latest_personalee(howmany=5):
    all_personalee = Personalee.objects.all().order_by('-date')[:howmany]
    return dict(all_personalee=all_personalee)

@register.inclusion_tag('Personalee/incontent_news.html')
def incontent_latest_personalee(howmany=5):
    all_personalee = Personalee.objects.all().order_by('-date')[:howmany]
    return dict(all_personalee=all_personalee)