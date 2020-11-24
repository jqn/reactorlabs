from django.urls import path
from . import views

urlpatterns = [
    path('api/capture/', views.LeadListCreate.as_view()),
]
