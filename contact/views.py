from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm
from .models import ContactModel
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Contact(LoginRequiredMixin, View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name, email, subject, message = cd['name'], cd['email'], cd['subject'], cd['message']
            ContactModel.objects.create(name=name, email=email, subject=subject, message=message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['pourabbaszahra3@gmail.com']
            send_mail(subject, name+': '+'\n'+message+'\n'+email, email_from, recipient_list)
        return render(request, 'contact/contact.html', {'form': form})