from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=255,unique=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    show_in_nav_list = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
            return self.slug

    def __unicode__(self):
        return self.title
