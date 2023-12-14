from django import forms
from django.core.exceptions import ValidationError
from .models import User


class SignUp(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your Email",
        'name': "email",
        'required': 'required',
    }))


class CheckTokenForm(forms.Form):
    code = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your Code",
               'name': "code",
               'required': 'required'
               }))


class SetInfo(forms.Form):
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'type': 'date',
               'placeholder': "Your Birth Day",
               'name': "birthday",
               'required': 'required'
               }))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your name",
               'name': "name",
               'required': 'required'
               }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your last name",
               'name': "last_name",
               'required': 'required'
               }))
    father_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your father name",
               'name': "father_name",
               'required': 'required'
               }))
    personal_id = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your personal id",
        'name': "personal_id",
        'required': 'required'
    }))
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your password",
        'name': "pass1",
        'required': 'required'
    }))
    pass2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Repeat password",
        'name': "pass2",
        'required': 'required'
    }))

    def clean(self):
        pass1 = self.cleaned_data['pass1']
        pass2 = self.cleaned_data['pass2']
        if pass1 != pass2:
            raise ValidationError('your entry passwords must be same!', code='dont_same_pass')


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your Email",
        'name': "email",
        'required': 'required',
    }))
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your password",
        'name': "pass1",
        'required': 'required'
    }))


class UpdateUserForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'type': 'date',
               'placeholder': "Your Birth Day",
               'name': "birthday",

               }))
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your name",
               'name': "name",

               }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your last name",
               'name': "last_name",

               }))
    father_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control border-white p-3",
               'placeholder': "Your father name",
               'name': "father_name",

               }))
    personal_id = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your personal id",
        'name': "personal_id",
    }))

    class Meta:
        model = User
        fields = [
            'date_of_birth',
            'name',
            'last_name',
            'father_name',
            'personal_id',
        ]


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control border-white p-3",
                                                                     'placeholder': "Your personal id",
                                                                     'name': "old_pass",
                                                                     'placeholder': "old password",
                                                                     'required': "required",
                                                                     }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control border-white p-3",
                                                                     'placeholder': "Your personal id",
                                                                     'name': "pass1",
                                                                     'placeholder': "Your password",
                                                                     'required': "required",
                                                                  }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control border-white p-3",
                                                                     'placeholder': "Your personal id",
                                                                     'name': "pass2",
                                                                     'placeholder': "Repeat your password",
                                                                     'required': "required",
                                                                  }))

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('your entry passwords must be same!', code='dont_same_pass')


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control border-white p-3",
        'placeholder': "Your Email",
        'name': "email",
        'required': 'required',
    }))
