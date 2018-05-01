from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=100)
    category=models.ManyToManyField(max_length=100)
    created=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(auto_now_add==True)

    is_published=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Entry(models.Model):
    post=models.OneToOneField(Post)
    headline=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.headline

class Category(models.CharField):
    name=models.CharField(max_lenth=100)

# User

    