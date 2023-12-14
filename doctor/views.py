from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
import datetime
from . import models


class SearchDoctor(View):
    def get(self, request):
        request = self.request
        date = datetime.datetime.strptime(request.GET.get('date'), '%m/%d/%Y')
        service = request.GET.get('service')
        doctors = models.Doctor.objects.filter(service__name=service, day__day=date.strftime('%A'))
        return render(request, 'doctor/search_doctor.html', {'doctors': doctors})


class ServicesAndPrices(View):
    def get(self, request):
        return render(request, 'doctor/service_price.html', {'service': models.Service.objects.all()})


class DoctorsCertificate(TemplateView):
    template_name = 'doctor/certificates.html'


class Team(TemplateView):
    template_name = 'doctor/teams.html'


def doctor_detail(request, pk):
    doctor = models.Doctor.objects.get(id=pk)
    return render(request, 'doctor/doctor-detail.html', {'doctor': doctor})


