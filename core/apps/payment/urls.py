from django.urls import path

from .views import AtmosCallbackApiView, PaymentGenerateLinkApiView, VisaMastercardPaymentApiView

urlpatterns = [
    path('callback/', AtmosCallbackApiView.as_view()),
    path('payment/', PaymentGenerateLinkApiView.as_view()),
    path('visa_mastercard/payment/', VisaMastercardPaymentApiView.as_view()),
]