import random 

from rest_framework import generics, views
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from core.apps.accounts import serializers
from core.apps.accounts import models
from core.apps.accounts.cache import cache_user_credentials, cache_user_confirmation_code
from core.apps.accounts.tasks import send_confirmation_code_to_email


class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            email = data['email']
            cache_user_credentials(
                email=email, password=data['password'],
                passport_id=data['passport_id'], pnfl=data['pnfl'], time=60*5
            )
            code = ''.join([str(random.randint(0, 100)%10) for _ in range(5)])
            cache_user_confirmation_code(
                email=email, code=code, time=60*5
            )
            send_confirmation_code_to_email.delay(email, code)
            return Response(
                {'success': True, 'message': "code sent"},
                status=200
            )
        

class ConfirmUserApiView(generics.GenericAPIView):
    serializer_class = serializers.ConfirmUserSerializer
    queryset = models.User.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response(
                {'access': str(token.access_token), 'refresh': str(token)},
                status=200
            )
        return Response(
            {'success': False, 'error_message': serializer.errors},
            status=400
        )