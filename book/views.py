from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from book.permisions import IsOwnerOrAdmin
from book.serializers import BookSerializer


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list all books or create a new book. Allows filtering by title, genre, and author name

    **Permissions**:
    - Read: Everyone
    - Create: Authenticated users
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("title", "genre__name", "author__name")


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a book by its ID.

    **Permissions**:
    - Read: Everyone
    - Update/Delete: Owner of the book or an Admin
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrAdmin]


class AvailableBooksListView(generics.ListAPIView):
    """
    API endpoint to list all available books.

    **Permissions**:
    - Read: Everyone
    """
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a book by its ID.

    **Permissions**:
    - Read: Everyone
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]