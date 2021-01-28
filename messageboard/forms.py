from django import forms
from django.core.exceptions import ValidationError
from api.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'text', 'phone_number', 'ad_category')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != int(11):
            raise ValidationError('Phone number length is less than 11 symbols')
        elif not phone_number.isdigit():
            raise ValidationError('Phone number contains forbidden symbols')
        return phone_number
