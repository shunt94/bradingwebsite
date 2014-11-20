from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from hellodjango.apps.brading.models import *
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


def issue(request, issue_id):
    issue_obj = Task.objects.get(pk=issue_id)
    parent = issue_obj.parent
    children = Task.objects.filter(parent=issue_obj)

    content = {
        'issue': issue_obj,
        'children': children,
        'parent': parent,
    }

    return render_to_response(
        'issue.html',
        content,
        context_instance=RequestContext(request)
    )


def issue_tracker(request):
    issues = Task.objects.all()
    jordans = []
    connors = []
    simons = []
    other = []
    jordan_time = 0
    connor_time = 0
    simon_time = 0
    for i in issues:
        if i.assignee == Task.JORDAN or i.assignee2 == Task.JORDAN or i.assignee3 == Task.JORDAN and not i.parent:
            jordans.append(i)
            jordan_time += i.time_spent
        if i.assignee == 'Simon' or i.assignee2 == 'Simon' or i.assignee3 == 'Simon' and not i.parent:
            simons.append(i)
            simon_time += i.time_spent
        if i.assignee == 'Connor' or i.assignee2 == 'Connor' or i.assignee3 == 'Connor' and not i.parent:
            connors.append(i)
            connor_time += i.time_spent
        if i.assignee == 'Unassigned' and i.assignee2 == 'Unassigned' and i.assignee3 == 'Unassigned':
            other.append(i)



    content = {
        'jordans_issues': jordans,
        'simons_issues': simons,
        'connors_issues': connors,
        'other': other,
        'connor_time': connor_time,
        'simon_time': simon_time,
        'jordan_time': jordan_time,
    }
    return render_to_response(
        'issuetracker.html',
        content,
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