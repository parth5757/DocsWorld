from django.urls import path, include
from .views import HEIFPNGAPIView, TestAPIView

urlpatterns = [
    path("test/", TestAPIView.as_view(), name="test"),
]