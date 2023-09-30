from django.db import models
from django.conf import settings
from book_supporting_resources.models import Author, Genre, Condition


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_books')
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="book_images/", null=True, blank=True)

    def book_location(self):
        return self.owner.location

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
