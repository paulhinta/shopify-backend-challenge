from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MemberCreationForm(UserCreationForm):
    email   = forms.EmailField(required=False)

    class Meta:     #tells us which other model will be affected
        model       = User
        fields      = [
            'username',
            'email',
            'password1',
            'password2'
        ]