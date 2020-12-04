# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('thanks/', HomePageView.as_view(), name='thanks'),
    path('', HomePageView.as_view(), name='home'),
]
