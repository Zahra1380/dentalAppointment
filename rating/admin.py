from django.contrib import admin
from .models import Rating
# Register your models here.


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'score']