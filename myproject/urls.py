from django.contrib import admin
from django.urls import path, include

# ✅ Swagger imports
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# ✅ JWT imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Your apps
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
    path('media/', include('media.urls')),

    # ✅ JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ✅ API Documentation (Swagger)
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
