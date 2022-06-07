from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    """Все операции для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

