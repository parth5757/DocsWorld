from django.contrib import admin
from django.urls import path, include
from docs_world.docs_world import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("image.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)