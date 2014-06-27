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
    url(r'^connor_private/$', 'hellodjango.apps.brading.views.connor_private',
        name="connor_private"),
    url(r'^invalid_group/$', 'hellodjango.apps.brading.views.invalid_group',
        name="invalid_group"),
)
