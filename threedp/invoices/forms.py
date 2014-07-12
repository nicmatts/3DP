from django import forms

from invoices.models import Invoice

class InvoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		#actual_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
		widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':50}),
        }