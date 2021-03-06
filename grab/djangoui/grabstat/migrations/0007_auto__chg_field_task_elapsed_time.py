# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Task.elapsed_time'
        db.alter_column(u'grabstat_task', 'elapsed_time', self.gf('django.db.models.fields.IntegerField')(default=0))

    def backwards(self, orm):

        # Changing field 'Task.elapsed_time'
        db.alter_column(u'grabstat_task', 'elapsed_time', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'grabstat.task': {
            'Meta': {'object_name': 'Task'},
            'elapsed_time': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'error_traceback': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'record_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'spider_stats': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spider_timing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'task_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        }
    }

    complete_apps = ['grabstat']