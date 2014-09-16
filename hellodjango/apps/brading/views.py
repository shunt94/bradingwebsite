from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from hellodjango.apps.brading.models import Bookmark, List, Project, Skill
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def home(request):
    return render_to_response(
        'index.html',
        {},
        context_instance=RequestContext(request)
    )


def portfolio(request):
    return render_to_response(
        'portfolio.html',
        {},
        context_instance=RequestContext(request)
    )


#Contact in nav bar
def about(request):
    return render_to_response(
        'about.html',
        {},
        context_instance=RequestContext(request)
    )


def jordan(request):
    return render_to_response(
        'jordan.html',
        {},
        context_instance=RequestContext(request)
    )


def simon(request):
    try:
        simon_user = User.objects.get(username="shunt94")
        projects = Project.objects.filter(user=simon_user)
    except User.DoesNotExist:
        projects = None

    return render_to_response(
        'simon.html',
        {'projects': projects,
         'skills': Skill.objects.all()},
        context_instance=RequestContext(request)
    )


def connor(request):
    return render_to_response(
        'connor/connor.html',
        {},
        context_instance=RequestContext(request)
    )


def connor_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="connor_swain_cv.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10, 10, "Hello, this is Connor")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def connor_contact(request):
    return render_to_response(
        'connor/contact.html',
        {},
        context_instance=RequestContext(request)
    )


def connor_education(request):
    return render_to_response(
        'connor/education.html',
        {},
        context_instance=RequestContext(request)
    )


def connor_hobbies(request):
    return render_to_response(
        'connor/hobbies.html',
        {},
        context_instance=RequestContext(request)
    )


def connor_projects(request):
    try:
        connor_user = User.objects.get(username="connor")
        projects = Project.objects.filter(user=connor_user).order_by('-start_date')
    except User.DoesNotExist:
        projects = None

    return render_to_response(
        'connor/projects.html',
        {"projects": projects},
        context_instance=RequestContext(request)
    )


def connor_work_experience(request):
    return render_to_response(
        'connor/work_experience.html',
        {},
        content_type=RequestContext(request)
    )


@login_required
def keep(request):
    lists = List.objects.filter(users=request.user)
    content = {
        'lists': lists,
    }
    return render_to_response(
        "keep.html",
        content,
        context_instance=RequestContext(request)
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
        'connor/private.html',
        content,
        context_instance=RequestContext(request)
    )


def invalid_group(request):
    return render_to_response(
        'invalid_group.html',
        {},
        context_instance=RequestContext(request)
    )