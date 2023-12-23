import factory
from django.contrib.auth.models import User

from djblogapp.models import Post


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    password = "123"
    username = "admin"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"
