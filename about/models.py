from django.db import models

class Day(models.Model):
    day = models.CharField(max_length=9)
    def __str__(self):
        return self.day

class ScheduleTime(models.Model):
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        return f'{self.time_in} - {self.time_out}'

class Open_Close(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='days')
    open = models.TimeField(null=True, blank=True)
    close = models.TimeField(null=True, blank=True)
    at_all_close = models.BooleanField(null=True, blank=True)
    schedule_time = models.ManyToManyField(ScheduleTime, related_name='open_close', null=True)

    def __str__(self):
        return f'{self.day}'

class Address(models.Model):
    state = models.CharField(max_length=500)
    city_name = models.CharField(max_length=500)
    rest_add = models.TextField()
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    telegram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.city_name} - {self.phone} - {self.email}'

class ItemAbout(models.Model):
    item_title = models.CharField(max_length=500)

    def __str__(self):
        return self.item_title

class AboutModel(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    explanation = models.TextField()
    items = models.ManyToManyField(ItemAbout, related_name='about')
    img = models.ImageField(null=True, upload_to='about/')

    def __str__(self):
        return self.title