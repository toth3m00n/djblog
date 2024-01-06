import pytest

pytestmark = pytest.mark.django_db


class TestPostModels:

    def test_str_return(self, post_factory):
        post = post_factory(title="test_post_title")
        assert str(post) == "test_post_title"

    def test_add_tags(self, post_factory):
        test = post_factory(title="test_post_title", tags=["test_post_tag"])
        assert test.tags.count() == 1
