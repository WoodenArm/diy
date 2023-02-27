from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        ordering = ["time_create"]
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'post_slug': self.slug})


class Photos(models.Model):
    title = models.CharField(max_length=200)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/", blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.title


class Comments(models.Model):
    text = models.TextField(verbose_name='Коментар')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, db_index=True, blank=True, verbose_name='URL')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Comments"