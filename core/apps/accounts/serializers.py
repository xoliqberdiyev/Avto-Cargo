from django.db import transaction

from rest_framework import serializers

from core.apps.accounts.models import User
from core.apps.accounts.cache import get_user_credentials, get_user_confirmation_code


class RegisterSerializer(serializers.Serializer):
    passport_id = serializers.CharField(required=False)
    pnfl = serializers.CharField(required=False)
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            request = self.context.get('request')
            lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en').split(",")[0]

            messages = {
                'en': "User with this email already exists",
                'ru': "Пользователь с таким адресом электронной почты уже существует",
                'uz': "Bu email bilan foydalanuvchi allaqachon mavjud",
            }
            msg = messages.get(lang, messages['en'])
            raise serializers.ValidationError(msg)
        return value
    

class ConfirmUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.IntegerField()

    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('User with this email already exists')
        user_data = get_user_credentials(email=data.get('email'))
        print(user_data)
        if not user_data:
            raise serializers.ValidationError("User with this email not found")
        confirm_data = get_user_confirmation_code(data['email'], data['code'])
        if not confirm_data:
            raise serializers.ValidationError("Invalid confirmation code")
        data['user_data'] = user_data
        return data
        
    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.get('user_data')
            user = User.objects.create(
                email=user_data.get('email'),
                passport_id=user_data.get('passport_id'),
                pnfl=user_data.get('pnfl'),
            )
            user.set_password(user_data.get('password'))
            user.save()
            return user
        