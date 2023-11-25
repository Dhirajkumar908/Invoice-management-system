from django import forms
from .models import *

class InvoiceForm(forms.ModelForm):
    class Meta:
        model:Invoice
        fields:["Client_details","product_details","price","quantity","discount","sub_total"]
