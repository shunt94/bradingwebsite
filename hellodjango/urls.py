from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hellodjango.apps.brading.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^jordan/$','hellodjango.apps.brading.views.jordan', name='jordan'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^connor/$', 'hellodjango.apps.brading.views.connor', name='connor'),
    url(r'^emma/$', 'hellodjango.apps.brading.views.emma', name='emma'),
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
    url(r'^accounts/', include('registration.backends.default.urls')),

)
