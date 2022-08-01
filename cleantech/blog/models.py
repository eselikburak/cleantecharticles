from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField


def unique_slug(instance, slug):
    model = instance.__class__
    unique_slug = slug
    counter = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slugify(slug + str(counter))
        counter += 1

    return unique_slug


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, editable=False)

    def __str__(self):
        return self.name

    # This save method is overriding save method!
    def save(self, *args, **kwargs) -> None:

        self.slug = unique_slug(self, slugify(self.name))
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=200, verbose_name='Title')
    content = RichTextField(blank=True, null=True, verbose_name='Content')
    published_date = models.DateTimeField(default=timezone.now, editable=False)
    last_update = models.DateTimeField(null=True, blank=True, editable=False)
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d/', blank=True, default='images/blog/default_post_image.jpg')
    is_available = models.BooleanField(default=True, verbose_name='Is Available')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Categories')
    slug = models.SlugField(unique=True, editable=False)


    # This save method is overriding save method!
    def save(self, *args, **kwargs) -> None:
        
        self.last_update = timezone.now()
        self.slug = unique_slug(self, slugify(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
