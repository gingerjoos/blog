from django.db import models

class Category(models.Model):

    term = models.CharField(max_length=255,unique=True)
    parent = models.ForeignKey('self',blank=True,null=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.term
