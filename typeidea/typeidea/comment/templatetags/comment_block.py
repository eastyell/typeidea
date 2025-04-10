from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()


@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,  # 评论目标
        'comment_form': CommentForm(),  # 评论内容
        'comment_list': Comment.get_by_target(target)  # 回复列表
    }
