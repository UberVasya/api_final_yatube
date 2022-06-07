from rest_framework import routers
from django.urls import include, path
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(
    r'^posts/(?P<post_pk>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
