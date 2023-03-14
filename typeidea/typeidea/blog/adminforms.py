from dal import autocomplete
from django import forms
from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )

    class Meda:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'content', 'status')
