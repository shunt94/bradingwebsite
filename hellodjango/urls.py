from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'hellodjango.apps.brading.views.home', name='home'),

    url(r'^jordan/$','hellodjango.apps.brading.views.jordan', name='jordan'),
    url(r'^portfolio/$','hellodjango.apps.brading.views.portfolio', name='portfolio'),
    url(r'^about/$','hellodjango.apps.brading.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^connor/$', 'hellodjango.apps.brading.views.connor', name='connor'),
    url(r'^simon/$', 'hellodjango.apps.brading.views.simon', name='simon'),
    url(r'^connor/private/$', 'hellodjango.apps.brading.views.connor_private',
        name="connor_private"),
    url(r'^connor/contact/$', 'hellodjango.apps.brading.views.connor_contact',
        name="connor_contact"),
    url(r'^connor/education/$', 'hellodjango.apps.brading.views.connor_education',
        name="connor_education"),
    url(r'^connor/hobbies/$', 'hellodjango.apps.brading.views.connor_hobbies',
        name="connor_hobbies"),
    url(r'^connor/projects/$', 'hellodjango.apps.brading.views.connor_projects',
        name="connor_projects"),
    url(r'^connor/work_experience/$', 'hellodjango.apps.brading.views.connor_work_experience',
        name="connor_work_experience"),
    url(r'^invalid_group/$', 'hellodjango.apps.brading.views.invalid_group',
        name="invalid_group"),
    url(r'^keep/$', 'hellodjango.apps.brading.views.keep',
        name="keep"),
    url(r'connor/pdf/$', 'hellodjango.apps.brading.views.connor_pdf',
        name="connor_pdf"),
    url(r'issuetracker/$', 'hellodjango.apps.brading.views.issue_tracker',
        name='issue_tracker'),
    url(r'issue/(?P<issue_id>[0-9]+)/$', 'hellodjango.apps.brading.views.issue',
        name='issue'),
    url(r'^accounts/', include('registration.backends.default.urls')),

)
