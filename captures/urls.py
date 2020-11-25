from django.urls import path
from . import views


urlpatterns = [
    path('captures/', views.index),
]
