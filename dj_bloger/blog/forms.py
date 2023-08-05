from django import forms
from tinymce.widgets import TinyMCE

from .models import Blog


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 30, }))

    class Meta:
        model = Blog
        fields = ['title', 'content', 'url', 'cat', 'image']

        # js = ('https://cdn.tiny.cloud/1/6h3aiuyj42f0vly6sd11kjl8ok6fw5na0vv4b66ayb3mmriw/tinymce/6/tinymce.min.js',
        #       'js/main.js')

# class UpdateForm(forms.ModelForm):
#     content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 30, } ))
#     url = forms.CharField( widget=forms.TextInput(attrs={'value':''}),disabled=True,)
#
#     class Meta:
#         model = Blog
#         fields = ['title', 'content','url', 'cat', 'image']
