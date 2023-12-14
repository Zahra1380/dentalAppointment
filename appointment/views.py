from django.shortcuts import render
from django.views.generic import View
from doctor.models import Doctor, Service
from about.models import ScheduleTime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

class MakeAppointment(LoginRequiredMixin, View):
    def get(self, request):
        serv = ''
        service = self.request.GET.get('service')
        if service:
            serv = Service.objects.get(slug=service).name
        return render(request, 'appointment/appointment.html',
                      {'service': Service.objects.all(), 'doctor': Doctor.objects.all(),
                       'times': ScheduleTime.objects.all(), 'serv_choise': serv})

    def post(self, request):
        request = self.request
        lst_doctor = request.POST.get('doctor').split('-')
        serv = request.POST.get('service')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor = Doctor.objects.filter(name=lst_doctor[0].strip(), service__name=serv)
        if not doctor:
            return render(request, 'appointment/appointment.html',
                          {'service': Service.objects.all(), 'doctor': Doctor.objects.all(),
                           'times': ScheduleTime.objects.all(),
                           'error': 'this doctor does not do this service, or your entry date was wrong!'})
        else:

            subject = f'appointment for {serv}'
            message = f'appointment for {serv} of {" ".join(lst_doctor)} for date {date} at {time} the peitien name: {name}{lastname} the phone and email of peitient is {phone}, {email} is submited'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, 'pourabbaszahra3@gmail.com']
            send_mail(subject, message, email_from, recipient_list)

            return render(request, 'appointment/appointment.html',
                          {'service': Service.objects.all(), 'doctor': Doctor.objects.all(),
                           'times': ScheduleTime.objects.all(),
                           'success': 'your ask appointment send, the clinic call you.'})

