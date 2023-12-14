from django.urls import path, include
from . import views

app_name = 'rating'
urlpatterns = [
    path('', views.DoctorRating.as_view (), name='rating'),
]
