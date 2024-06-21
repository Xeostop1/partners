from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    objects = models.Manager()  # Default manager
