from rest_framework import generics, views
from rest_framework.response import Response

from core.apps.accounts import serializers
from core.apps.accounts import models
from core.apps.accounts.cache import cache_user_credentials

class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = models.User.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            cache_user_credentials(
                email=data['email'], password=data['password'],
                passport_id=data['passport_id'], pnlf=data['pnlf'], time=60*5
            )
            return Response(
                {'success': True, 'message': "code sent"},
                status=200
            )