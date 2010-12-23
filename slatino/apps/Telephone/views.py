from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from slatino.apps.Personalee.models import Personalee

from slatino.apps.Telephone.models import Phone

def telephone_list(request):
    all_phone = Phone.objects.all()
    personalee = get_object_or_404(Personalee)
    phone_list = Phone.objects.filter(personalee=personalee)
    heading = "Personalee: %s" % personalee.name
    return render_to_response("Telephone/list.html", locals())
