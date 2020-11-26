from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(null=True, blank=True, default='')
    time = models.DateTimeField(default=timezone.now)

    class   Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.title

