from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    order_number = serializers.IntegerField()
    price = serializers.IntegerField()

    