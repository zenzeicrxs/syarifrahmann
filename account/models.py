from django.db import models

# Create your models here.
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    percentage = models.IntegerField(default=0, help_text='Percentage of skill level (0-100)')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    status = models.IntegerField(choices=[
        (0, 'Draft'),
        (1, 'Published'),
    ], default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
