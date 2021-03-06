# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'notes_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('urgent', self.gf('django.db.models.fields.BooleanField')()),
            ('resolved', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'notes', ['Note'])

        # Adding model 'Update'
        db.create_table(u'notes_update', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('note', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notes.Note'])),
        ))
        db.send_create_signal(u'notes', ['Update'])


    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'notes_note')

        # Deleting model 'Update'
        db.delete_table(u'notes_update')


    models = {
        u'notes.note': {
            'Meta': {'object_name': 'Note'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resolved': ('django.db.models.fields.BooleanField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'urgent': ('django.db.models.fields.BooleanField', [], {})
        },
        u'notes.update': {
            'Meta': {'object_name': 'Update'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['notes.Note']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['notes']