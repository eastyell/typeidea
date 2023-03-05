from django.contrib.auth.models import User
from django.db import models
from common.constant import *


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '2-分类'

    def __str__(self):
        return self.name

    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
            'navs': nav_categories,
            'categories': normal_categories,
        }


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '3-标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name= "标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ManyToManyField(Tag, verbose_name="新标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    pv = models.PositiveIntegerField(default=1)  # 访问量
    uv = models.PositiveIntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "1-文章"
        ordering = ['-id']

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=STATUS_NORMAL)\
                .select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=STATUS_NORMAL)\
                .select_related('owner', 'category')
        return post_list, category

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=STATUS_NORMAL)
        return queryset

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=STATUS_NORMAL).order_by('-pv')




