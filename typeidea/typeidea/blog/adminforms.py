from dal import autocomplete
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10, 'style': 'border: 2px solid red'}),
                           label='摘要', required=False, )
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tag = forms.ModelChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )

    content = forms.CharField(widget=CKEditorWidget(), label='正文', required=True) # 富文本

    class Meda:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'content', 'status')
