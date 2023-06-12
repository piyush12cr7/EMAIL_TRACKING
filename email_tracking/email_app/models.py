from django.db import models

# Create your models here.
from django.db import models

class Email(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, default='Queued')

    def __str__(self):
        return self.subject