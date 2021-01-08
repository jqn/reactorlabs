from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')

    def validate_email(self, value):
        qs = Lead.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this email already exists")
        return value
