from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _

from slatino.apps.Transport.models import Transport, Raspisanie, Ceni
from string import join

def transport_list(request):
    all_transport = Transport.objects.all()
    page = {'title':"All transport"}
    return render_to_response("Transport/list.html", {"all_transport":all_transport,
                                                 "page":page})

def raspisanie_show(request, raspisanie_id):
    all_raspisanie = Raspisanie.objects.all()
    page = {'title':"Raspisanie"}
    raspisanie = get_object_or_404(Raspisanie, id=raspisanie_id)
    return render_to_response("Transport/one.html", {"all_raspisanie":all_raspisanie, "raspisanie":raspisanie,
                                                 "page":page})
def ceni_show(request):
    all_ceni = Ceni.objects.all()
    page = {'title':"Ceni"}
    return render_to_response("Transport/one.html", {"all_ceni":all_ceni,
                                                 "page":page})
