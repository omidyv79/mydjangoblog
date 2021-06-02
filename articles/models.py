from django.db import models
from django.db.models.fields import DateField, SlugField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    Slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    #in add thumbtail
    #add in author
    def __str__(self) :
        return self.title
    
    def snippet (self) :
        return self.body[:50]  + ' ...'