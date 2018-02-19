from django.urls import path, include,re_path
from django.views.generic import ListView, DetailView
from testapp.models import TestFields

urlpatterns = [
    path('', ListView.as_view(queryset=TestFields.objects.all()[:20],
    template_name="testapp/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model= TestFields, template_name="testapp/post.html")),
]
