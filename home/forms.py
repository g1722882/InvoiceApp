from django import forms
from django.forms import formset_factory
from .models import Invoice
class InvoiceForm(forms.Form):
    
    seller_name = forms.CharField(
        label='sellerName',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seller Name',
            'rows':1,
            'name': 'Seller Name',
        })
    )
    
    
    
    buyer_name = forms.CharField(
        label='buyerName',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buyer Name',
            'rows':1,
            'name': 'Buyer Name',
        })
    )
    
    
    
    
    
    seller_phone = forms.CharField(
        label='phoneNumber',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
            'rows':1,
            'name': 'Seller Phone',
        })
    )
    
    
    buyer_phone = forms.CharField(
        label='buyerNumber',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone Number',
            'rows':1,
            'name': 'Buyer Phone',
        })
    )
    
    
    
    seller_billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'rows':1,
            'name': 'Seller Billing Address',
        })
    )
    
    
    buyer_billing_address = forms.CharField(
        label='Billing Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'rows':1,
            'name': 'Buyer Billing Address',
        })
    )
    
    
    
    
    
    
    

class LineItemForm(forms.Form):
    
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Book Name here',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )
    amount = forms.DecimalField(
        disabled = True,
        label='Amount $',
        widget=forms.TextInput(attrs={
        'class': 'form-control input',
     })
    )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)