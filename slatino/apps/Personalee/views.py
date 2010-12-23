from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from slatino.apps.Personalee.models import Personalee


def personalee_list(request):
    all_personalee = Personalee.objects.all()
    page = {'last_name': "All personalee"}
    return render_to_response("Personalee/list.html", context_instance=RequestContext(request, {"all_personalee": all_personalee, "page": page}))


def personalee_show(request, personalee_id):
    personalee = get_object_or_404(Personalee, id=personalee_id)
    return render_to_response("Personalee/one.html", context_instance=RequestContext(request, {"personalee": personalee}))


def personalee_show_spec(request, slug):
    page = {}
    if slug=="last":
        all_personalee = Personalee.objects.all()
        page['last_name'] = _("Last personalee")
    else:
        Http404()
    return render_to_response("Personalee/list.html", context_instance=RequestContext(request, {"all_personalee": all_personalee,
                                                 "page": page}))
