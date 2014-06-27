from django.db import models


class Bookmark (models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)