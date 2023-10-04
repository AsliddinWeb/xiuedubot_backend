from django.contrib import admin
from django.urls import path, include

from .views import home

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Swagger UI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="XIU EDU BOT | API",
      default_version='v1',
      description="Xiu edu bot",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('info_app.urls')),

    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
