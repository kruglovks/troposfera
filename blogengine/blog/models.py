"""docstring"""
from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """docstring"""
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=120, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
        