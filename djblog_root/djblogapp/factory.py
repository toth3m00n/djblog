from random import randint

import factory
import faker
from django.contrib.auth.models import User

from .models import Post

FAKE = faker.Faker()
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=randint(2, 12))
    subtitle = factory.Faker("sentence", nb_words=randint(2, 12))
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="admin")[0]

    @factory.lazy_attribute
    def content(self):
        x = ""
        for _ in range(5):
            x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return x

    status = "published"