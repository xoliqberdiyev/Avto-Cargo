from django.urls import path

from .views import AtmosCallbackApiView, PaymentGenerateLinkApiView

urlpatterns = [
    path('callback/', AtmosCallbackApiView.as_view()),
    path('payment/', PaymentGenerateLinkApiView.as_view()),
]