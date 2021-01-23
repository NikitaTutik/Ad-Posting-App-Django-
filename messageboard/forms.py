from django import forms
from api.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'text', 'phone_number')