from django.contrib import admin
from . import models

@admin.register(models.Service)
class AdminService(admin.ModelAdmin):
    list_display = ('name', 'cost', 'slug')

@admin.register(models.DentalExperts)
class AdminDentalExperts(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Doctor)
class AdminDoctor(admin.ModelAdmin):
    list_display = ('name', 'last_name')

@admin.register(models.Certificate)
class CertificateDoctor(admin.ModelAdmin):
    list_display = ('doctor', 'image', 'explanation')