from django.db import models
from django.conf import settings


class Genre(models.Model):
	name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=255)
	
	def __str__(self):
		return self.name


class Condition(models.Model):
	NEW = 'New'
	USED = 'Used'
	
	CONDITION_CHOICES = (
		(NEW, 'New'),
		(USED, 'Used')
	)
	
	condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=NEW)
	
	def __str__(self):
		return self.condition


class Book(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_books')
	location = models.CharField(max_length=255)
	is_available = models.BooleanField(default=True)
	
	# TODO: Make Class For this
	# recipient = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
	#                                    related_name='book_requesters')
	
	# TODO: Add Image
	# image = ""
	
	def __str__(self):
		return self.title
