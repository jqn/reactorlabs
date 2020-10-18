from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, generics, permissions

from .models import EmailCapture
from .serializers import EmailCaptureSerializer

# django corsheaders cfe.sh


class EmailCaptureCreateAPIView(generics.CreateAPIView):
    queryset = EmailCapture.objects.all()
    serializer_class = EmailCaptureSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        request = self.request
        user = request.user
        if not user.is_authenticated:
            user = None  # Annon User
        serializer.save(user=user)
