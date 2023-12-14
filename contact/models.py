from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.subject}'
