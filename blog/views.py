from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    MonthArchiveView
)
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import MultipleObjectMixin
# Create your views here.


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_new.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_edit.html'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')


class BlogListView(ListView):
    model = Post
    paginate_by = 1
    template_name = 'blog/posts.html'
    # Takes care of error
    # Pagination may yield inconsistent results with an unordered object_list
    ordering = ['-created_on']
    # queryset = Post.objects.all()

    # def get_queryset(self):
    #     return Post.objects.filter(
    #         featured=True, draft=False).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Post.objects.filter(
            headline=True, draft=False).last()
        context['featured'] = Post.objects.filter(
            featured=True, draft=False).order_by('-last_modified')[0:2]
        context['firehose'] = Post.objects.filter(
            firehose=True, draft=False).last()
        context['posts'] = Post.objects.filter(
            headline=False, featured=False, firehose=False, draft=False).order_by('-created_on')[:4]
        context['categories'] = Category.objects.all()
        context['archives'] = Post.objects.dates(
            'last_modified', 'month', order='DESC')
        return context


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


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "publish"
    allow_empty = True
