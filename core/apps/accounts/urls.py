from django.urls import path, include

from core.apps.accounts import views

urlpatterns = [
    path('login/', views.CustomTokenObtainPairView.as_view()),
    path('register/', views.RegisterApiView.as_view()),
    path('confirm_user/', views.ConfirmUserApiView.as_view()),
]