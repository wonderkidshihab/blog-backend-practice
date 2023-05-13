from django.urls import include, path
from django.views.generic import TemplateView
urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/index.html")),
    path('api/', include('blog_api.urls')),
]
