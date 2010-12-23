from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from slatino.apps.Links.models import Links
from string import join

 
def links_list(request):
    all_links= Links.objects.all().order_by('-pub_date')
    print all_links
    page = {'title':_("All links")}

    #print request.LANGUAGE_CODE

    return render_to_response("Links/list.html", RequestContext(request, {"all_links":all_links,
                                                 "page":page}))

def link_show(request, link_id):
    link = get_object_or_404(Links, id=link_id)
    return render_to_response("Links/one.html", RequestContext(request, {"link":link}))
    
