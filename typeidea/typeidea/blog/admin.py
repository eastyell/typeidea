from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeideabase.custom_site import custom_site
from typeideabase.base_admin import BaseOwnerAdmin


# Register your models here.
class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = (PostInline,)
    list_display = ('name', 'status', 'is_nav', 'post_count', 'owner', 'create_time')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()  # post的model存在一个到ModelA的外键，自动为ModelA反向生成一个字段

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'create_time')
    fields = ('name', 'status')


# define the filer show only you
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = (
        'title', 'category', 'status',
        'create_time', 'owner', 'operator'
    )
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # edit page
    # save_on_top = True
    exclude = ('owner',)
    # fields = (
    #     ('title', 'category',),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('',),
            'fields': ('tag',),
        })
    )

    filter_horizontal = ('tag',)

    # filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # def get_app_list(self, request):
    #     """
    #     Return a sorted list of all the installed apps that have been
    #     registered in this site.
    #     """
    #     ordering = {
    #         "文章": 1,
    #         "分类": 2,
    #         "标签": 3,
    #     }
    #     app_dict = self._build_app_dict(request)
    #     # a.sort(key=lambda x: b.index(x[0]))
    #     # Sort the apps alphabetically.
    #     app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    #     # Sort the models alphabetically within each app.
    #     for app in app_list:
    #         app['Post'].sort(key=lambda x: ordering[x['name']])
    #     return app_list

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message', 'action_time']
