from django.db import transaction

from rest_framework import serializers

from core.apps.accounts.models import User
from core.apps.accounts.cache import get_user_credentials


class RegisterSerializer(serializers.ModelSerializer):
    passport_id = serializers.CharField()
    pnfl = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists")
        if get_user_credentials(value):
            raise serializers.ValidationError("User with this email already exists")
        return value