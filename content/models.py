from django.db import models
from django.contrib.auth.models import User
from taxonomy.models import Category

class Post(models.Model):

    title = models.CharField(max_length=255,unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category)
    is_published = models.BooleanField(default=True)
    comments_allowed = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
            return self.category.slug + '/' + self.slug

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
