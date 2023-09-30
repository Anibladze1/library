from django.db import models
from django.conf import settings
from book_supporting_resources.models import Author, Genre, Condition


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_books')
    is_available = models.BooleanField(default=True)

    def book_location(self):
        return self.owner.location

    # TODO: Add Image
    # image = ""

    def __str__(self):
        return self.title
