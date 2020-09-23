from django.db import models


# Create your models here.
class Task(models.Model):
    text = models.TextField()
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.id} - {self.text}")
