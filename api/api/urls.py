from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LittleURL API",
        default_version='v1',
        description="API of LittleURL application",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # SWAGGER
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    # DJANGO ADMIN
    path('admin/', admin.site.urls),

    # APPLICATIONS
    path('api/auth/', include('authentication.urls')),
    path('api/little-urls/', include('mylittleurl.urls')),
]
