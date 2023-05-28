from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from blog.models import Category, IsAuthorOrReadOnly, Post
from django.contrib.auth.models import User

from .serializers import CategorySerializer, PostSerializer, PostCreateSerializer


class PostList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('category', )
    ordering_fields = ('title', 'category', 'published')
    
    def perform_create(self, serializer):
        # Set the author field with the user associated with the access token
        serializer.save(author=User.objects.get(pk=1))
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostSerializer
        
    
    
class PostDetail(generics.RetrieveDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        return PostCreateSerializer
    
class CategoryList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class CategoryDetail(generics.RetrieveDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
