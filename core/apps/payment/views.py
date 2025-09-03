import hashlib

from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from core.apps.orders.models import Order
from core.apps.payment.serializers import PaymentSerializer
from core.services.payment import Atmos


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class AtmosCallbackApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        client_ip = get_client_ip(request)
        # if client_ip not in settings.ALLOWED_ATMOS_IPS:
        #     return Response({"status": 0, "message": "IP ruxsat etilmagan"}, status=403)
        data = request.data
        if not data:
            return Response(
                {'success': 0, "message": "Request body required"},
                status=status.HTTP_200_OK
            )

        store_id = data.get("store_id")
        transaction_id = data.get("transaction_id")
        invoice = data.get("invoice")
        amount = data.get("amount")
        sign = data.get("sign")

        check_string = f"{store_id}{transaction_id}{invoice}{amount}{settings.API_KEY}"
        generated_sign = hashlib.sha256(check_string.encode()).hexdigest()

        if generated_sign != sign:
            return Response(
                {"status": 0, "message": f"Инвойс с номером {invoice} отсутствует в системе"},
                status=status.HTTP_200_OK
            )

        try:
            order = Order.objects.get(order_number=invoice)
        except Order.DoesNotExist:
            return Response(
                {"status": 0, "message": f"Инвойс с номером {invoice} отсутствует в системе"},
                status=status.HTTP_200_OK
            )

        if str(order.total_price) != str(amount):
            return Response(
                {"status": 0, "message": f"Инвойс с номером {invoice} отсутствует в системе"},
                status=status.HTTP_200_OK
            )

        order.is_paid = True
        order.save()

        return Response(
            {"status": 1, "message": "Успешно"},
            status=status.HTTP_200_OK
        )


class PaymentGenerateLinkApiView(GenericAPIView):
    serializer_class = PaymentSerializer
    queryset = None
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'success': False, 'message': serializer.errors}, status=400)
        data = serializer.validated_data
        service = Atmos()
        res = service.create_transaction(data['price'], data['order_number'])
        link = service.generate_url(res['transaction_id'], 'https://wisdom.uz')
        return Response(
            {"success": True, "url": link},
            status=200
        )

