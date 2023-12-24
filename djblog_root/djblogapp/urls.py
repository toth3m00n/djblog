from django.urls import path

from djblog.settings import local
from djblogapp.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='homepage')
]

