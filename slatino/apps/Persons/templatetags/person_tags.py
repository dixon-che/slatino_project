from django import template
from slatino.apps.Persons.models import Person
register = template.Library()


@register.inclusion_tag('Person/box_news.html')
def pull_latest_person(howmany=5):
    all_person = Person.objects.all().order_by('-date')[:howmany]
    return dict(all_person=all_person)


@register.inclusion_tag('Person/incontent_news.html')
def incontent_latest_person(howmany=5):
    all_person = Person.objects.all().order_by('-date')[:howmany]
    return dict(all_person=all_person)
