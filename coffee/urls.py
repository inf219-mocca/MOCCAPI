from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import APIViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="MOCCA API",
        default_version="v1",
        description="MOCCA API Documentation",
        contact=openapi.Contact(email="sni038@student.uib.no"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = "coffee"
urlpatterns = [
    path("coffee/", APIViewSet.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
