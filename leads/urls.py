from django.urls import path
from . import views

urlpatterns = [
    path('api/leads/', views.LeadListCreate.as_view()),
]
