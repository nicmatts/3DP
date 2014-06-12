from django.contrib import admin
from invoices.models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer_filename', 'id')

admin.site.register(Invoice, InvoiceAdmin)