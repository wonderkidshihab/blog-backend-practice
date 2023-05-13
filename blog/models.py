from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Custom permission class for users. A user can read all posts, but only edit and delete their own posts.
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post.
        return obj.author == request.user





# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
        
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=(("draft", "Draft"), ("published", "Published")), default="published")
    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ("-published",)
        
    def __str__(self):
        return self.title
