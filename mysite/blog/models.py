from __future__ import unicode_literals

# my imports
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# create a model called post

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    # slug is for urls, to create beautiful and simple urls for blog posts.
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

# meta stands for meta data, we are asking djang to display content by date plubished.
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title