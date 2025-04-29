from django.db import models


class Todo(models.Model):
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item
