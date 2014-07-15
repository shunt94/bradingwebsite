from django.db import models
from registration.models import User


class Bookmark (models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % self.name


class List(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=255)


class ListItem(models.Model):
    text = models.CharField(max_length=255)
    list = models.ForeignKey(List, related_name="items")
