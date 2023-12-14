import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import User, ValidateCode
import uuid
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from validate_email import validate_email
from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import timedelta, datetime
from . import forms
import shortuuid

# Create your views here.


class SignUp(View):
    def get(self, request):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            return redirect('home:home')
        else:
            form = forms.SignUp()
            return render(request, 'account/base_page.html', {'form': form})

    def post(self, request):
        form = forms.SignUp(request.POST)

        if form.is_valid() and validate_email(form.cleaned_data['email']):
            email = form.cleaned_data['email']
            token = uuid.uuid4()
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            code = random.randint(1000, 9999)
            send_mail('your email validation code', f'your email validation code is: {code}', email_from,
                      recipient_list)
            ValidateCode.objects.create(email=email, token=token, code=code)
            return redirect(reverse('account:register') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid phone')
        return render(request, 'account/base_page.html', {'form': form})


class CheckToken(View):
    def get(self, request):
        form = forms.CheckTokenForm()
        return render(request, 'account/base_page.html', {'form': form})

    def post(self, request):
        form = forms.CheckTokenForm(request.POST)
        if form.is_valid():
            token = request.GET.get('token')
            code = form.cleaned_data.get('code')
            if ValidateCode.objects.filter(token=token, code=code).exists():
                validation = ValidateCode.objects.get(token=token)
                if datetime.now(validation.expration_date.tzinfo) - validation.expration_date > timedelta(minutes=5):
                    form.add_error('code', 'code was intropt!')
                    validation.delete()
                    print('delete')
                else:
                    User.objects.create_user(email=validation.email)
                    return redirect(reverse('account:set-info') + f'?token={token}')
        else:
            form.add_error('code', 'invalid code')
        return render(request, 'account/base_page.html', {'form': form})


class SetInfoView(View):
    def get(self, request):
        form = forms.SetInfo()
        return render(request, 'account/base_page.html', {'form': form})
    def post(self, request):
        form = forms.SetInfo(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            token = request.GET.get('token')
            validation = ValidateCode.objects.get(token=token)

            user = User.objects.get(email=validation.email)
            date_of_birth = cd['date_of_birth']
            name = cd['name']
            last_name = cd['last_name']
            father_name = cd['father_name']
            personal_id = cd['personal_id']
            pass1 = cd['pass1']
            pass2 = cd['pass2']
            user.set_password(pass1)
            user.date_of_birth = date_of_birth
            user.name = name
            user.last_name = last_name
            user.father_name = father_name
            user.personal_id = personal_id
            user.save()
            login(request, user)
            validation.delete()
            return redirect(reverse('home:home'))
        else:
            form.add_error('name', 'invalid code')
        return render(request, 'account/base_page.html', {'form': form})

class SignIn(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('home:home')
        else:
            form = forms.SignInForm()
            return render(request, 'account/base_page.html', {'form': form})
    def post(self, request):
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            next = request.GET.get('next')

            user = authenticate(email=cd['email'], password=cd['pass1'])
            if user:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('home:home')

        else:
            form.add_error('email', 'invalid code')
        return render(request, 'account/base_page.html', {'form': form})
class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home:home'))


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)
        print(user_form)
        print(user_form.errors)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user_form.save()
            return redirect(reverse_lazy('home:home'))
    else:
        user_form = forms.UpdateUserForm(instance=request.user)

    return render(request, 'account/base_page.html', {'form': user_form})


class ChangePassword(LoginRequiredMixin,View):
    def get(self, request):
        form = forms.ChangePasswordForm()
        return render(request, 'account/base_page.html', {'form': form})

    def post(self, request):
        form = forms.ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['old_password'])
            try:
                user = authenticate(username=self.request.user.email, password=cd['old_password'])
                print(user)
                user.set_password(cd['password1'])
                user.save()
                return redirect(reverse('home:home'))
            except:
                form.add_error('old_password', 'your entry old password was wrong!')
        return render(request, 'account/base_page.html', {'form': form})

class ForgetPassword(View):
    message = ''

    def get(self, request):
        form = forms.ForgetPasswordForm()
        return render(request, 'account/base_page.html', {'form': form, 'message': self.message})

    def post(self, request):
        form = forms.ForgetPasswordForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                user = User.objects.get(email=email)
                password = shortuuid.uuid()
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail('your password', f'your password is: {password}\nyou should change your password after login!', email_from,
                          recipient_list)
                user.set_password(password)
                user.save()
                self.message = ('your password change and send it to you from the email!')
                return redirect(reverse_lazy('account:sign-in'))
            except:
                form.add_error('email', 'this email does not exists')
        return render(request, 'account/base_page.html', {'form': form, 'message': self.message})
