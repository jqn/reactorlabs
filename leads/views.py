from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics

# Create your views here.


class LeadListCreate(generics.ListCreateAPIView):
    print("hello world")
    queryset = Lead.objects.all()
    print(queryset)
    serializer_class = LeadSerializer
