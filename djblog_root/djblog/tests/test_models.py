import pytest

pytestmark = pytest.mark.django_db


class TestPostModels:

    def test_str_return(self, post_factory):
        post = post_factory(title="test_post_title")
        assert str(post) == "test_post_title"
