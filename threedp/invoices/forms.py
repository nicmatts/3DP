from django import forms

from invoices.models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice