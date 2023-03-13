from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post
from common.constant import *


class PostSitemap(Sitemap):
    changefred = 'always'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.create_time

    def location(self, obj):
        return reverse('post-detail', args=[obj.pk])