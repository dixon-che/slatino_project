from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.utils.translation import ugettext as _
from slatino.apps.Institute.models import Institute, Occupation


def institute_list(request):
    all_institute = Institute.objects.all()
    page = {'title': "All institute"}
    return render_to_response("Institute/list.html", RequestContext(request, {"all_institute": all_institute, "page": page}))


def institute_show(request, institute_id):
    all_occupation = Occupation.objects.all()
    institute = get_object_or_404(Institute, id=institute_id)
    return render_to_response("Institute/one.html", RequestContext(request, {"institute": institute, "all_occupation": all_occupation}))


def institute_show_spec(request, slug):
    page = {}
    if slug == "last":
        all_institute = Institute.objects.all()
        page['title'] = _("Last institute")
    else:
        Http404()
    return render_to_response("Institute/list.html", RequestContext(request, {"all_institute": all_institute, "page": page}))
