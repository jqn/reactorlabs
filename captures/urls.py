from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/captures/', views.EmailCaptureCreateAPIView.as_view()),
    path('', views.CapturesPageView.as_view()),
]
