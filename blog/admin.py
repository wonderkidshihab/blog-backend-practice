from django.contrib import admin

from blog.models import Category, Post

# Register your models here.
admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to Blog Portal"
admin.site.register(Post)
admin.site.register(Category)