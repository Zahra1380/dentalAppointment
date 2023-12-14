from django.contrib import admin
from .models import BlogModel, Visitors


# Register your models here.
@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image_tag',
        'user',
        'publish_date',
    ]


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = [
        'visitors',
        'blog',
    ]
