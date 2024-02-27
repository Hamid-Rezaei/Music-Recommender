from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

open_api_urlpatterns = [
    # Our PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

public_urlpatterns = [
    path('api/v1/', include('main.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = open_api_urlpatterns + public_urlpatterns
