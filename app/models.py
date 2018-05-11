from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class PostManager(models.Manager):
    """
    POST.objects
    重载get_queryset,默认查询确认发布的文章
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Post(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ManyToManyField(Category)

    created = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.name


class Entry(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    content = models.TextField()


# User
class UserExtends(models.Model):
    class Meta:
        abstract = True
