from django.urls import path, include,re_path
from django.views.generic import ListView, DetailView
from news.models import News

urlpatterns = [
    path('', ListView.as_view(queryset=News.objects.all().order_by("-published_date")[:20],
    template_name="news/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model= News, template_name="news/post.html")),
]
