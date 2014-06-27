from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from hellodjango.apps.brading.models import Bookmark


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


def connor(request):
    return render_to_response(
        'connor.html',
        {},
        content_type=RequestContext(request)
    )


@login_required
def connor_private(request):
    try:
        group = Group.objects.get(name="to_view_connors_page")
    except Group.DoesNotExist:
        return HttpResponseRedirect('/invalid_group/')
    if not group in request.user.groups.all():
        HttpResponseRedirect('/invalid_group/')
    bookmarks = Bookmark.objects.all()
    content = {
        'bookmarks': bookmarks,
    }
    return render_to_response(
        'connor_private.html',
        content,
        content_type=RequestContext(request)
    )


def invalid_group(request):
    return render_to_response(
        'invalid_group.html',
        {},
        content_type=RequestContext(request)
    )