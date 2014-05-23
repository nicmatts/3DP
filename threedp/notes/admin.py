from django.contrib import admin
from notes.models import Note
from notes.models import Update

class NoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created', 'resolved', 'urgent')
    list_filter = ['created']
    search_fields = ['subject']

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created',)
    list_filter = ['created']
    search_fields = ['subject']

admin.site.register(Note, NoteAdmin)

admin.site.register(Update, UpdateAdmin)