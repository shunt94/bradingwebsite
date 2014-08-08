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


class Project(models.Model):
    WORK = "glyphicon-briefcase"
    UNI = "glyphicon-book"
    HOME = "glyphicon-home"
    icon_choices = (
        (WORK, WORK),
        (UNI, UNI),
        (HOME, HOME),
    )
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    icon = models.CharField(max_length=55, choices=icon_choices, blank=False)
    completed = models.BooleanField(default=False, blank=False)
    skills = models.TextField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title