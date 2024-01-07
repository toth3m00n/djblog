from django.shortcuts import render, get_object_or_404
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


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "djblogapp/single_post.html", {"post": post, "related": related})
