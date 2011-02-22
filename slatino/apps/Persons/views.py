from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from slatino.apps.Persons.models import Person


def person_list(request):
    all_person = Person.objects.all()
    page = {'last_name': "All person"}
    return render_to_response("Persons/list.html", RequestContext(request, {"all_person": all_person, "page": page}))


def person_show(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    return render_to_response("Persons/one.html", RequestContext(request, {"person": person}))


def person_show_spec(request, slug):
    page = {}
    if slug == "last":
        all_person = Person.objects.all()
        page['last_name'] = _("Last person")
    else:
        Http404()
    return render_to_response("Persons/list.html", RequestContext(request, {"all_person": all_person, "page": page}))
