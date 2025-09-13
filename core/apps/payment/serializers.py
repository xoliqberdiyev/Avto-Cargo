from rest_framework import serializers

from core.apps.orders.models import Order


class PaymentSerializer(serializers.Serializer):
    order_number = serializers.IntegerField()
    price = serializers.IntegerField()

    def validate_order_number(self, value):
        if not Order.objects.filter(order_number=value).exists():
            raise serializers.ValidationError("Order not found")
        return value


class VisaPaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    order_number = serializers.IntegerField()

    def validate_order_number(self, value):
        if not Order.objects.filter(order_number=value).exists():
            raise serializers.ValidationError("Order not found")
        return value