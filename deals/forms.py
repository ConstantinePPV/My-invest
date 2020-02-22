from django import forms
from .models import Deal


class DealForm(forms.ModelForm):

    class Meta:
        model = Deal
        fields = (
            'date_deal', 
            'stock', 
            'price_deal', 
            'volume_deal',
        )