from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db import models
from typeidea.typeidea.common.constant import *


# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    href = models.URLField(verbose_name="链接")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,
                                         verbose_name="状态")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6),
                                         range(1, 6)), verbose_name="权重",
                                         help_text="权重高展示顺序靠前")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"


class SideBar(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE,
                                               verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容",
                               help_text="如果设置的不是html类型，可为空")
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS,
                                         verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间 ")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=STATUS_SHOW)

    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment
        result = ''
        if self.display_type == DISPLAY_HTML:
            result = self.content
        elif self.display_type == DISPLAY_LATEST:
            context = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', context)
        elif self.display_type == self.DISPLAY_HOT:
            context = {
                'posts': Post.hot_posts()
            }
            result = render_to_string('config/blocks/sidebar_posts.html', context)
        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                'comments': Comment.objects.filter(status=STATUS_NORMAL)
            }
            result = render_to_string('config/blocks/sidebar_comments.html', context)
        return result
