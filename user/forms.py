from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'first_name', 'email', 'phone', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            #self.fields[fieldname].widget.attrs['placeholder'] = self.fields[fieldname].label
            self.fields[fieldname].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Ваш логин'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ваше имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Ваш e-mail'
        self.fields['phone'].widget.attrs['placeholder'] = 'Ваш телефон'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ваш пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите ваш пароль'
