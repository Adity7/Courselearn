from django.conf import settings
from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.TextField()
    author = models.TextField()
    overview = models.TextField()
    image = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title