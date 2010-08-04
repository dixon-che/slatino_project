from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from tagsfield.models import Tag

def index(request):
    return render_to_response("main.html",{"main":"main"})

def tag(request, slug):
    tag = get_object_or_404(Tag, value=slug)
    return render_to_response("tag.html",{"tag":tag})

def robots(request):
    text = '''User-agent: *
Disallow: /admin
Host: slatino.in.ua'''
    return HttpResponse(text)

