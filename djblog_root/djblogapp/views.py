from django.shortcuts import render
from django.views.generic import ListView

from djblogapp.models import Post


class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "djblogapp/components/post-list-elements.html"
        return "djblogapp/index.html"
