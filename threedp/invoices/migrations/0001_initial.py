# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invoice'
        db.create_table(u'invoices_invoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('customer_first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('customer_last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('customer_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('customer_phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('customer_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('customer_filename', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('customer_purpose', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('customer_department', self.gf('django.db.models.fields.CharField')(max_length=5, null=True)),
            ('sd_card_number', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('estimated_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('estimated_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('actual_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('job_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('job_state', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'invoices', ['Invoice'])


    def backwards(self, orm):
        # Deleting model 'Invoice'
        db.delete_table(u'invoices_invoice')


    models = {
        u'invoices.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'actual_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer_department': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'customer_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'customer_filename': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'customer_first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'customer_last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'customer_phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'customer_purpose': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'customer_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'estimated_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'job_state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sd_card_number': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['invoices']