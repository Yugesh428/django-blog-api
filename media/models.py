from django.db import models


class MediaFile(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    file = models.FileField(upload_to='media/files/', null=True, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
