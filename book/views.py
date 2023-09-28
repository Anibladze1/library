from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Book, Author, Genre, Condition
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer
from .filters import BookFilter


# Author Views
class AuthorsListCreateView(generics.ListCreateAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


# Genre Views
class GenresListCreateView(generics.ListCreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


# Book Views
class BookListCreateView(generics.ListCreateAPIView):
	serializer_class = BookSerializer
	filter_class = BookFilter
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	def get_queryset(self):
		return Book.objects.all()
	
	# def perform_create(self, serializer):
	# 	serializer.validated_data.pop('recipient', None)
	# 	serializer.save(owner=self.request.user)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


# Condition Views
class ConditionCreateView(generics.CreateAPIView):
	queryset = Condition.objects.all()
	serializer_class = ConditionSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class AvailableBooksListView(generics.ListAPIView):
	queryset = Book.objects.filter(is_available=True)
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


