from django.contrib import admin

# Register your models here.
from hellodjango.apps.brading.models import Bookmark

admin.site.register(Bookmark)