from django.db import models
from doctor.models import Doctor
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
# Create your models here.
class Rating(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='star_rate',)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    def __str__(self):
        return f'{self.doctor.name}: {self.score}'