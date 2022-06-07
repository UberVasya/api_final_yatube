from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, filters
from posts.models import Post, Group, Follow, User
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, \
    FollowSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    """Все операции для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Все операции для комментов"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, id=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр групп."""
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = None

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Group.objects.all()
        return Group.objects.filter(pk=pk)


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    """Кастомный класс для работы с подписками"""

    pass


class FollowViewSet(ListCreateViewSet):
    """Просмотр и создание подписки"""
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following = get_object_or_404(
            User, username=self.request.data['following']
        )
        serializer.save(user=self.request.user, following=following)
