from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from skycards_api.views import CreateCardView, GetCardView

schema_view = get_schema_view(
    openapi.Info(
        title="Skycards API",
        default_version='v1',
        description="description",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('card/', CreateCardView.as_view()),
    path('card/<int:pk>', GetCardView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
