from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    url_enter = forms.CharField()
