from rest_framework import serializers

from accounts.serializers import UserSerializer
from blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class PostSerializer(serializers.ModelSerializer):
    
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "author", "excerpt", "content", "status", "slug", "category", "published", "thumbnail"]
        read_only_fields = ["id", "author"]
        
        
class PostCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False)
    class Meta:
        model = Post
        fields = ["id", "title", "author", "excerpt", "content", "status", "slug", "category", "thumbnail"]
        read_only_fields = ["id", "author"]