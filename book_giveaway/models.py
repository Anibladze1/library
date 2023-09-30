from django.db import models

from book.models import Book
from library import settings


class AskForBookRequest(models.Model):
	requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requester")
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
	request_date = models.DateTimeField(auto_now_add=True, blank=True)
	is_confirmed = models.BooleanField(default=False)
	
	def __str__(self):
		return f"{self.requester.username} is requesting for {self.book.title}"
