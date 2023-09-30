from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Book
from book.permisions import IsOwnerOrAdmin
from book.serializers import BookSerializer
from book.filters import BookFilter


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrAdmin]


class AvailableBooksListView(generics.ListAPIView):
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
