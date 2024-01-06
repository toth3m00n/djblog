from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag('djblogapp/components/tag_cloud.html')
def sidebar_tag_cloud():
    tags = Tag.objects.all()
    return {'tags': tags}
