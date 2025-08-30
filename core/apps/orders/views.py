from rest_framework import generics, permissions
from rest_framework.response import Response

from core.apps.orders import serializers, models


class OrderListApiView(generics.GenericAPIView):
    serializer_class = serializers.OrderListSerializer
    queryset = models.Order.objects.select_related('location_to', 'location_from')
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = models.Order.objects.filter(user=request.user)
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=200)
