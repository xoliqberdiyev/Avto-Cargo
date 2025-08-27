import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.apps.orders.models import Order

API_KEY = "ATMOS_API_KEY"  
ALLOWED_ATMOS_IPS = ["185.8.212.47"]


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
        if client_ip not in ALLOWED_ATMOS_IPS:
            return Response({"status": 0, "message": "IP ruxsat etilmagan"}, status=403)
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

        check_string = f"{store_id}{transaction_id}{invoice}{amount}{API_KEY}"
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
