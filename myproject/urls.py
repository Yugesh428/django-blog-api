from django.contrib import admin
from django.urls import path, include

# ✅ add this import
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from django.contrib import admin
from django.urls import path, include

# ✅ Swagger imports
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Your apps
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
    path('media/', include('media.urls')),   # ✅ ADDED

    # ✅ API Documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]