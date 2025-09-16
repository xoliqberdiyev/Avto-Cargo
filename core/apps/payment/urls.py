from django.urls import path

from .views import AtmosCallbackApiView, PaymentGenerateLinkApiView, VisaMastercardPaymentApiView, PayPaymeApiView

urlpatterns = [
    path('callback/', AtmosCallbackApiView.as_view()),
    path('payment/', PaymentGenerateLinkApiView.as_view()),
    path('visa_mastercard/payment/', VisaMastercardPaymentApiView.as_view()),
    path('payme/', PayPaymeApiView.as_view()),
]