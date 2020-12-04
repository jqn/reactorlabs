from django.urls import path
from .views import EmailCaptureView


urlpatterns = [
    path('newsletter/signup', EmailCaptureView.as_view(), name="captures"),
]
