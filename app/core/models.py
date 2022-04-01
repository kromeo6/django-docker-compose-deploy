from django.db import models

# Create your models here.
class Sample(models.Model):
    attachment = models.FileField()

class Chat(models.Model):
    session_id = models.CharField(max_length=500)
    dt = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return f"Message '{self.message}' "