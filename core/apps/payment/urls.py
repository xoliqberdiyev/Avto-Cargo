from django.urls import path

from .views import AtmosCallbackApiView

urlpatterns = [
    path('callback/', AtmosCallbackApiView.as_view()),
]