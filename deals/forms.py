from django import forms
from .models import Deal


class DateInput(forms.DateInput):
    input_type = 'date'


class DealForm(forms.ModelForm):

    class Meta:
        model = Deal
        fields = (
            'date_deal', 
            'stock', 
            'price_deal', 
            'volume_deal',
            'sum_deal',
        )   
        widgets = {'date_deal': DateInput()}