from django import forms
from .models import Payment

class FormulariPagament(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'expiration_date', 'cvc']
