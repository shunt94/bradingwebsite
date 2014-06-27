from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response(
        'index.html',
        {},
        content_type=RequestContext(request)
    )


def jordan(request):
    return render_to_response(
        'jordan.html',
        {},
        content_type=RequestContext(request)
    )