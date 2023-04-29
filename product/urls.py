from django.urls import path,include
from rest_framework import routers
from .views import CatagoryViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"category", CatagoryViewSet)


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs', SpectacularSwaggerView.as_view(url_name = "schema"), name='schema_docs'),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
