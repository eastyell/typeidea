from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Link
from common.constant import *


# Create your views here.
class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'