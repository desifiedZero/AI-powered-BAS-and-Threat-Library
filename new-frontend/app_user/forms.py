from django import forms


class NewSettingsForm(forms.Form):
    password = forms.CharField(label='Password')