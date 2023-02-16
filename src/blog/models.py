from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    description = models.TextField(default='')
    content=models.TextField(default='')