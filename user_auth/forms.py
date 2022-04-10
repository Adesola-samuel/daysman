from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from academy.models import Biodata

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={}))
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm password'


class UserLoginForm(forms.Form):
    username = forms.ChoiceField(widget=forms.TextInput())
    password = forms.ChoiceField(widget=forms.PasswordInput())

class BioForm(forms.ModelForm):
    model=Biodata
    fields = '__all__'


