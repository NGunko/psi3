from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    created = models.DateField(default=datetime.date.today)
    tooltip = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'



class Workflow(models.Model):
    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=512, default='')
    category = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    versionInit = models.CharField(max_length=128)
    client_ip = models.GenericIPAddressField()
    keywords = models.CharField(max_length=256, default='')
    json = models.CharField(max_length=128)
    created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Workflow, self).save(*args, **kwargs)
