# TODO:  Напишите свой вариант
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from rest_framework import generics, status, viewsets, permissions, filters

from rest_framework.response import Response
from .models import Post, Comment, Group, Follow
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter


from .permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = PostFilter

    def get_queryset(self): 
        queryset = Post.objects.all() 
        return queryset 
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer): 
        serializer.save(author=self.request.user)
     



class GroupViewSet(viewsets.ModelViewSet):   
    serializer_class = GroupSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    def get_queryset(self): 
        queryset = Group.objects.all() 
        return queryset 
    def perform_create(self, serializer): 
        serializer.save() 
    def perform_update(self, serializer): 
        serializer.save() 



class CommentsViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def get_post(self): 
        post = get_object_or_404(Post, id=self.kwargs['post_id']) 
        return post 
    def get_queryset(self): 
        queryset = Comment.objects.filter(post=self.get_post()).all() 
        return queryset 
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user, post=self.get_post()) 
    def perform_update(self, serializer): 
        serializer.save(author=self.request.user, post=self.get_post()) 

class FollowViewSet(generics.ListCreateAPIView): 
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', '=user__username']
    
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user) 

