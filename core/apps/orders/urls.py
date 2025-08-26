from django.urls import path

from core.apps.orders import views

urlpatterns = [
    path('order/list/', views.OrderListApiView.as_view()),
]