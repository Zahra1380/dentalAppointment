from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control border-0 bg-light px-4", 'placeholder': "Your Name",
        'style': "height: 55px;", 'name': 'name', 'required': 'required',
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email", 'class': "form-control border-0 bg-light px-4", 'placeholder': "Your Email",
        'style': "height: 55px;",
        'name': 'email', 'required': 'required',
    }))
    subject = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control border-0 bg-light px-4", 'placeholder': "Subject",
        'style': "height: 55px;", 'name': 'subject', 'required': 'required',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control border-0 bg-light px-4 py-3", 'rows': "5", 'placeholder': "Message", 'name': 'subject',
        'required': 'required',
    }))
