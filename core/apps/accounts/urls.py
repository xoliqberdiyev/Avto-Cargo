from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

from core.apps.accounts import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.RegisterApiView.as_view()),
    path('confirm_user/', views.ConfirmUserApiView.as_view()),
]