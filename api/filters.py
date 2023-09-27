import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    owner = django_filters.NumberFilter(field_name="owner__id")
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'genre', 'condition', 'owner', 'location']
