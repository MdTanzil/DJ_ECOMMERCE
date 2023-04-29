from django.urls import path,include
from rest_framework import routers
from .views import CatagoryViewSet

router = routers.DefaultRouter()
router.register(r"category", CatagoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
