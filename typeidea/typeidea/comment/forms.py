from django import forms
import mistune

from .models import Comment


# 回复表单验证
class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵 称 ',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 10%;'}
        )
    )
    email = forms.CharField(
        label='Email ',
        max_length=100,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 10%;'}
        )
    )
    # website = forms.CharField(
    #     label='网 站 ',
    #     # label_suffix='',
    #     max_length=200,
    #     widget=forms.widgets.URLInput(
    #         attrs={'class': 'form-control', 'style': 'width: 10%;'}
    #     )
    # )
    content = forms.CharField(
        label='内 容 ',
        max_length=2000,
        widget=forms.widgets.Textarea(
            attrs={'rows': 10, 'cols': 40, 'class': 'form-control'}
        )
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度太短！')
        content = mistune.markdown(content)   # 渲染markdown效果
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'content']


