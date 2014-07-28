from django.contrib import admin

# Register your models here.
from hellodjango.apps.brading.models import Bookmark, ListItem, List, Project

admin.site.register(Bookmark)
admin.site.register(List)
admin.site.register(ListItem)
admin.site.register(Project)