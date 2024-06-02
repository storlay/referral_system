"""
URL configuration for referral project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',
         include(("users.api.urls", "users-api"), namespace="users-api")
         )
]

# Redoc
urlpatterns += [
    path('api/schema/',
         SpectacularAPIView.as_view(),
         name='schema'
         ),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'
         ),
]
