from django.urls import path, include
from . import views

app_name = 'doctor'
urlpatterns = [
    path('search-doctor', views.SearchDoctor.as_view(), name='search-doctor'),
    path('service-price', views.ServicesAndPrices.as_view(), name='service-price'),
    path('doctors-certificate', views.DoctorsCertificate.as_view(), name='doctors-certificate'),
    path('our-team', views.Team.as_view(), name='our-team'),
    path('doctor-detail/<int:pk>/', views.doctor_detail, name='doctor-detail'),
]
