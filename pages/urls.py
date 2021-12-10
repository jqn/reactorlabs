# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, VimCheatSheet

urlpatterns = [
    path('vim-cheat-sheet', VimCheatSheet.as_view(), name='vim-cheat-sheet'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('thanks/', HomePageView.as_view(), name='thanks'),
    path('', HomePageView.as_view(), name='home'),
]
