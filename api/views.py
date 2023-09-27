from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Book, Author, Genre, Condition
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer
from .filters import BookFilter


# Base view with overridden permissions
class ReadOnlyForUnauthenticated(generics.GenericAPIView):
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Author Views
class AuthorsListCreateView(ReadOnlyForUnauthenticated, generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(ReadOnlyForUnauthenticated, generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Genre Views
class GenresListCreateView(ReadOnlyForUnauthenticated, generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenresRetrieveUpdateDestroyView(ReadOnlyForUnauthenticated, generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Book Views
class BookListCreateView(ReadOnlyForUnauthenticated, generics.ListCreateAPIView):
    serializer_class = BookSerializer
    filter_class = BookFilter

    def get_queryset(self):
        return Book.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data.pop('recipient', None)
        serializer.save(owner=self.request.user)


class BookRetrieveUpdateDestroyView(ReadOnlyForUnauthenticated, generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Condition Views
class ConditionCreateView(ReadOnlyForUnauthenticated, generics.CreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class AvailableBooksListView(generics.ListAPIView):
    queryset = Book.objects.filter(recipient__isnull=True)
    serializer_class = BookSerializer


# Request Book Views

class RequestBookView(generics.UpdateAPIView, ReadOnlyForUnauthenticated):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        book = self.get_object()

        if book.recipient:
            return Response({"error": "This book is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        book.recipient = request.user
        book.save()

        return Response({"message": "You are now the recipient of the book"}, status=status.HTTP_200_OK)


class ReturnBookView(generics.UpdateAPIView, ReadOnlyForUnauthenticated):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        book = self.get_object()

        if book.recipient != request.user:
            return Response({"error": "Only the recipient can return the book"}, status=status.HTTP_403_FORBIDDEN)

        book.recipient = None
        book.save()

        return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)

