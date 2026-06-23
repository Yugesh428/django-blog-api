from django.db import models

# Create your models here.
from django.db import models


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author
