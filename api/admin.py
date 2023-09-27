from django.contrib import admin
from .models import Condition, Book, Author, Genre

admin.site.register(Condition)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
