"""typeideabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.sitemaps import views as sitemap_views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .custom_site import custom_site
# from blog.views import post_list, post_detail
from blog.views import PostDetailView, IndexView, TagView, \
    CategoryView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.apis import post_list, PostList, PostViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')
urlpatterns = [
                  path('super_admin/', admin.site.urls, name='super-admin'),  # system users
                  path('admin/', custom_site.urls, name='admin'),  # business users
                  re_path(r'^$', IndexView.as_view(), name='index'),  # main webpage
                  # re_path(r'^$', post_list, name='index'),
                  # re_path(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
                  re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
                  # re_path(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
                  re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
                  # re_path(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
                  re_path(r'^post/(?P<pk>\d+).html$', PostDetailView.as_view(), name='post-detail'),
                  re_path(r'^links/$', LinkListView.as_view(), name='links'),
                  re_path(r'^search/', SearchView.as_view(), name='search'),
                  re_path(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
                  re_path(r'^comment/$', CommentView.as_view(), name='comment'),
                  re_path(r'^rss|feed/', LatestPostFeed(), name='rss'),
                  re_path(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
                  re_path(r'^category-autocomplete/$', CategoryAutocomplete.as_view(),
                          name='category-autocomplete'),  # 下拉框自动搜索
                  re_path(r'^tag-autocomplete/$', TagAutocomplete.as_view(),
                          name='tag-autocomplete'),  # 下拉框自动搜索
                  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 图片上传
                  # re_path(r'^api/post/', post_list, name='post-list'),
                  # re_path(r'^api/post/', PostList.as_view(), name='post-list'),
                  re_path(r'^api/', include((router.urls, 'api'), namespace='api')),  # rest_framework
                  # path('docs/', include_docs_urls(title='My API title')),
                  re_path(r'^api/docs/', include_docs_urls(title='typeidea apis')),  # rest_framework doc


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 调试优化
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [re_path(r'^debug/', include(debug_toolbar.urls)), ]


