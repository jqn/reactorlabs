from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'slug', 'cover', 'body', 'author',
                  'category', 'headline', 'featured', 'firehose', 'draft']
