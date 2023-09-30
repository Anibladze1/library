from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Author, Genre, Condition
from book.permisions import IsOwnerOrAdmin
from .serializers import AuthorSerializer, GenreSerializer, ConditionSerializer


# Author Views
class AuthorsListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrAdmin]


# Genre Views
class GenresListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsOwnerOrAdmin]


# Condition Views
class ConditionCreateView(generics.CreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
