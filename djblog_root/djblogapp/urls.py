from django.urls import path

from djblog.settings import local
from djblogapp import views
from djblogapp.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='homepage'),
    path("<slug:post>", views.post_single, name='post_single')
]

