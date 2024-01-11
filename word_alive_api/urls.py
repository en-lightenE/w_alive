from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions





urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
