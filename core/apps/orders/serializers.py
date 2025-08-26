from rest_framework import serializers

from core.apps.orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'name', 'date', 'status', 'size', 'total_price', 'is_paid', 'location'
        ]