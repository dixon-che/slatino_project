from django.shortcuts import render_to_response, get_object_or_404
from slatino.apps.Persons.models import Person
from slatino.apps.Telephone.models import Phone


def telephone_list(request):
    all_phone = Phone.objects.all()
    person = get_object_or_404(Person)
    phone_list = Phone.objects.filter(person=person)
    heading = "Person: %s" % person.name
    return render_to_response("Telephone/list.html", locals())
