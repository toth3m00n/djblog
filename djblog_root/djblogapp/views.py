from django.shortcuts import render
from django.views.generic import ListView

from djblogapp.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'djblogapp/index.html'
    context_object_name = "posts"
