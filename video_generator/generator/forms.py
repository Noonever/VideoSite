from django import forms

class CreateVideoForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, label='', widget=forms.TextInput({ "placeholder": "Name"}))