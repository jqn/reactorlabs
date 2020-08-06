from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/posts.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCategoryView(ListView):
    template_name = 'blog/post_category.html'
    context_object_name = 'posts'
    ordering = ['-last_modified']

    def get_queryset(self, *args, **kwargs):
        self.category = get_object_or_404(
            Category, name=self.kwargs['category'])
        return Post.objects.filter(categories__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the category
        context['category'] = self.category
        return context
