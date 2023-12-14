from django.contrib import admin
from . import models


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['day']


@admin.register(models.Open_Close)
class Open_CloseAdmin(admin.ModelAdmin):
    list_display = ['day', 'at_all_close']


@admin.register(models.ScheduleTime)
class AdminScheduleTime(admin.ModelAdmin):
    list_display = ('time_in', 'time_out')


@admin.register(models.Address)
class StateAdmin(admin.ModelAdmin):
    list_display = ['phone', 'city_name', 'email']


@admin.register(models.ItemAbout)
class ItemAboutAdmin(admin.ModelAdmin):
    list_display = ['item_title']


@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'subtitle', ]
