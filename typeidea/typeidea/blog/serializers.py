from rest_framework import serializers, pagination

from .models import Post, Category
from common.constant import *


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,

        slug_field='name'
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # url = serializers.HyperlinkedIdentityField(view_name='api-post-detail')

    class Meta:
        model = Post
        # url是明细链接
        fields = ['url', 'id', 'title', 'category', 'tag', 'owner', 'create_time']


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content_html', 'create_time']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'create_time',
        )


class CategoryDetailSerializer\
            (CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')  # 通过方法paginated_posts获取数据给post

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'create_time', 'posts'
        )


