from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),

    path('genres/', views.GenresListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', views.GenresRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy'),

    path('authors/', views.AuthorsListCreateView.as_view(), name='author-list-create'),
    path('author/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),

    path('create-condition/', views.ConditionCreateView.as_view(), name='create-condition'),

    path('request-book/<int:pk>/', views.RequestBookView.as_view(), name='request-book'),
    path('return-book/<int:pk>/', views.ReturnBookView.as_view(), name='return-book'),
    path("available-books/", views.AvailableBooksListView.as_view(), name='available-books')
]
