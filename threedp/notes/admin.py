from django.contrib import admin
from notes.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created', 'resolved', 'urgent')
    list_filter = ['created']
    search_fields = ['subject']

admin.site.register(Note, NoteAdmin)