from rest_framework import routers
from django.urls import include, path
from .views import PostViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
