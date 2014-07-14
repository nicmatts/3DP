from django.contrib import admin
from django.http import HttpResponse
from invoices.models import Invoice

import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d")

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=3DP-' + date +'.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"customer_filename"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.customer_filename),
        ])
    return response
export_csv.short_description = u"Export CSV"

def export_xlsx(modeladmin, request, queryset):
    import openpyxl
    from openpyxl.cell import get_column_letter
    response = HttpResponse(mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=3DP-' + date +'.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.get_active_sheet()
    ws.title = "3DP " + date

    row_num = 1

    columns = [
        (u"ID", 15),
        (u"Customer Filename", 70),
    ]

    for col_num in xrange(len(columns)):
        c = ws.cell(row=row_num, column=col_num+1)
        c.value = columns[col_num][0]
        #c.style.font.bold = True
        # set column width
        ws.column_dimensions[get_column_letter(col_num+1)].width = columns[col_num][1]

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.customer_filename,
        ]
        for col_num in xrange(len(row)):
            c = ws.cell(row=row_num, column=col_num+1)
            c.value = row[col_num]
            #c.style.alignment.wrap_text = True

    wb.save(response)
    return response

export_xlsx.short_description = u"Export XLSX"

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('customer_filename', 'created', 'id')
    actions = [export_csv, export_xlsx]


admin.site.register(Invoice, InvoiceAdmin)