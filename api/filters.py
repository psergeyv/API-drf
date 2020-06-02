from django_filters import rest_framework as filters
from .models import Post, Follow


class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        fields = ['group', ]
