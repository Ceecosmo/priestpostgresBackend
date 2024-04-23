from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("amount", "email", "creditors_FullName", "phone_number", "message")
        