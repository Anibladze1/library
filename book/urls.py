from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('book/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path("book/<int:pk>/detailview", views.BookDetailView.as_view(), name='book-detail-view'),
    path('book/available-books/', views.AvailableBooksListView.as_view(), name='available-books')

]
