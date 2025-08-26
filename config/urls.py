from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.permissions import IsAdminUser

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Avto Cargo API",
      default_version='v1',
      description="Avto Cargo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(IsAdminUser,),
)


urlpatterns = [
   path('admin/', admin.site.urls),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/v1/', include(
      [
         path('accounts/', include('core.apps.accounts.urls')),     
         path('common/', include('core.apps.common.urls')),
         path('orders/', include('core.apps.orders.urls')),
      ]
   ))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
