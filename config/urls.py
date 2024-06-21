from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Booking API",
        default_version='v1',
        description="Api Documentation of Booking",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include([
        path('swagger/', schema_view.with_ui('swagger',
             cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc',
             cache_timeout=0), name='schema-redoc'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
