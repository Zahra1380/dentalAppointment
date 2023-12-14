from django.shortcuts import render
from django.views.generic import View
from doctor.models import Service, Doctor
from about.models import ScheduleTime
# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home/index.html', {'service': Service.objects.all()})