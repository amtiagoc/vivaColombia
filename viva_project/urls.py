from django.contrib import admin
from django.urls import path, include
from viva_api.views import stories

urlpatterns = [
    path("admin/", admin.site.urls),
    path("top-stories", stories),
]
