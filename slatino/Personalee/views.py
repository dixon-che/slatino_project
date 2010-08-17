from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _

from slatino.Personalee.models import Personalee
from string import join

def personalee_list(request):
    all_personalee = Personalee.objects.all()
    page = {'name':"All personalee"}
    return render_to_response("Personalee/list.html", {"all_personalee":all_personalee,
                                                 "page":page})

def personalee_show(request, personalee_id):
    personalee = get_object_or_404(Personalee, id=personalee_id)
    return render_to_response("Personalee/one.html", {"personalee":personalee})

def personalee_show_spec(request, slug):
    page = {}
    if slug=="last":
        all_personalee = Personalee.objects.all()
        page['name'] = _("Last personalee")
    else:
        Http404()
    return render_to_response("Personalee/list.html", {"all_personalee":all_personalee,
                                                 "page":page})

