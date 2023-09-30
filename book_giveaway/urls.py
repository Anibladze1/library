from django.urls import path
from book_giveaway import views

urlpatterns = [
	path("request-book/", views.RequestBookView.as_view(), name='request-book'),
	path("books-requests/", views.GetBookRequestListView.as_view(), name='list-requests'),
	path("confirm-request/<int:pk>", views.ConfirmBookRequestView.as_view(), name='confirm-request'),
]