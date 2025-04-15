from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, \
    CategorySerializer, CategoryDetailSerializer
from common.constant import *


@api_view()
def post_list(request):
    posts = Post.objects.filter(status=STATUS_NORMAL)

    post_serializes = PostSerializer(posts, many=True)
    return Response(post_serializes.data)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=STATUS_NORMAL)
    serializer_class = PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """提供新闻接口"""
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=STATUS_NORMAL)
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
