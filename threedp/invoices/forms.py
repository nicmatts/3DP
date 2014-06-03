from django import forms

from invoices.models import Note

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Note