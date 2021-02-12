# articles/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(
        max_length=250, unique_for_date='publish', blank=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    headline = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    firehose = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.publish.year),
                                            str(self.publish.month),
                                            str(self.publish.day), self.slug])

    def get_markdown(self):
        body = self.body
        return mark_safe(markdown(body))
