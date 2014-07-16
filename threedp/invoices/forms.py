from django import forms

from invoices.models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':50}),
        }