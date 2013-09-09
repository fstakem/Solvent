from django.db import models
from os import popen

class User(models.Model):
    # Attributes
    name = models.CharField(max_length=200)
    date_joined = models.DateTimeField() 
    email = models.EmailField(max_length=75)
    web_site = models.URLField(max_length=200, blank=True)
    last_active = models.DateTimeField()

    # Relationships
    friend = models.ManyToManyField("self", related_name='friend', blank=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    # Attributes
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    last_activity = models.DateTimeField()

    # Relationships
    owner = models.ForeignKey(User, related_name='owned_project')
    contributor = models.ManyToManyField(User, related_name='contributed_project')

    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    # Attributes
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    last_modified = models.DateTimeField()
    data = models.FileField(upload_to='documents/%Y/%m/%d')

    # Relationships
    owner = models.ForeignKey(User, related_name='created_attachment')
    project = models.ForeignKey(Project, related_name='related_attachment')

    def __unicode__(self):
        return self.name

    def dataOverview(self):
        file_name = self.data.path.split('/')[-1]
        output = ''
        if file_name.endswith('txt') or file_name.endswith('py'):
            output = popen('tail ' + self.data.path).read()
        return output
