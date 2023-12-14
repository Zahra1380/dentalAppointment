from django.urls import path
from .views import About

app_name = 'about'
urlpatterns = [
    path('', About.as_view(), name='about-use' )
]
