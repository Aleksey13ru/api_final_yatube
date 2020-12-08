from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment, Follow, Group
from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)
from .permission import IsAuthorOrReadOnly


class PostGet(viewsets.mixins.CreateModelMixin,
               viewsets.mixins.ListModelMixin,
               viewsets.GenericViewSet):
    pass


class GroupViewSet(PostGet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticated]

    def get_post(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.get_post())
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(PostGet):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', '=user__username']

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
