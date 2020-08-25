# blog/urls.py
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogCategoryView,
    ArticleMonthArchiveView
)

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name="post_edit"),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('<int:year>/<int:month>/',
         ArticleMonthArchiveView.as_view(month_format='%m'), name="post_archive"),
    path('<category>/', BlogCategoryView.as_view(), name="post_category"),
    path('', BlogListView.as_view(), name='posts'),
]
