from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenresListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', views.GenresRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy'),

    path('authors/', views.AuthorsListCreateView.as_view(), name='author-list-create'),
    path('author/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author-retrieve-update-destroy'),

    path('create-condition/', views.ConditionCreateView.as_view(), name='create-condition'),
]
