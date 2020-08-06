# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCategoryView

urlpatterns = [
    path('', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('<category>/', BlogCategoryView.as_view(), name="post_category"),
]
