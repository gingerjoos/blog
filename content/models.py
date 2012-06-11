from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    is_published = models.BooleanField()
    comments_allowed = models.BooleanField()
    url = models.URLField(blank=True,null=True)
    author = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post)
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User,blank=True,null=True)
    body = models.TextField()
    is_approved = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body
