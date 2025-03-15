from django import forms
from .models import DailySale

class DailySaleForm(forms.ModelForm):
    class Meta:
        model = DailySale
        fields = ['product', 'amount_sold']

    def increment_sale(self):
        self.instance.amount_sold += 1
        self.instance.save()
