from django.db import models
from blog.models import Post
from common.constant import *


# Create your models here.
class Comment(models.Model):
    target = models.CharField(max_length=100, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models .URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
        ordering = ["-create_time"]

    # 帅选回复内容
    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=STATUS_NORMAL)
