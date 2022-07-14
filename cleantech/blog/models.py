from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=200, unique=True, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Blog Content')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d/')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')
    categories = models.ManyToManyField(Category, null=True, verbose_name='Categories')
    slug = models.SlugField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.slug = slugify(self.title)
        self.save()

    def __str__(self):
        return self.title
