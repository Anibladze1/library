from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

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
