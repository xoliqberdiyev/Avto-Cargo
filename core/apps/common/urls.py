from django.urls import path

from core.apps.common import views

urlpatterns = [
    path('site_config/', views.SiteConfigApiView.as_view()),
    path('about_us/', views.AboutUsApiView.as_view()),
    path('banners/', views.BannerListApiView.as_view()),
    path('services/', views.ServiceListApiView.as_view()),
    path('news/', views.NewsListApiView.as_view()),
    path('contact_us/', views.ContactUsApiView.as_view()),
    path('requisite/', views.RequisiteApiView.as_view()),
    path('privacy_policy/', views.PrivacyPolicyListApiView.as_view()),
    path('user_terms/', views.UserTermsListApiView.as_view()),
]