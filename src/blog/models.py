from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(default=slugify(name))


# Create your models here.
User
class BlogPost(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=slugify(title))
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(default='')
    content=models.TextField(default='')
    
        
        
    def published_string(self):
        if self.published:
            return "L'article est publié"
        
        return "L'article est inaccessible"
        