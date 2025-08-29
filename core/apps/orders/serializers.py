from rest_framework import serializers

from core.apps.orders.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    location_to = serializers.SerializerMethodField(method_name='get_location_to')
    location_from = serializers.SerializerMethodField(method_name='get_location_from')
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'name', 'date', 'status', 'size', 'total_price', 'is_paid', 'location', 'location_to',
            'location_from'
        ]

    def get_location_to(self, obj):
        return {
            'id': obj.location_to.id,
            'name': obj.location_to.name
        }

    def get_location_from(self, obj):
        return {
            'id': obj.location_from.id,
            'name': obj.location_from.name
        }