
from django.urls import path
from . import views

app_name = 'appointment'
urlpatterns = [
    path('make-appintment', views.MakeAppointment.as_view(), name='make-appintment'),
]