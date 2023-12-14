from django.db import models
from about.models import Day
from django.utils.text import slugify

class DentalExperts(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=500, unique=True)
    cost = models.FloatField()
    image = models.ImageField(upload_to='services', null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save()

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    expert = models.ForeignKey(DentalExperts, on_delete=models.CASCADE, related_name='doctors_expert')
    instagram = models.CharField(max_length=500)
    telegram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    img = models.ImageField(upload_to='doctors', default='/doctors/team-1.jpg')
    service = models.ManyToManyField(Service, related_name='doctors')
    day = models.ManyToManyField(Day, related_name='day_work')
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return f'{self.name} - {self.last_name}'


class Certificate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='certificate')
    image = models.ImageField(upload_to='certificate')
    explanation = models.TextField()

    def __str__(self):
        return self.explanation
