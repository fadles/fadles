# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'House.description'
        db.alter_column(u'fadles_house', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Product.additional_info'
        db.alter_column(u'fadles_product', 'additional_info', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):

        # Changing field 'House.description'
        db.alter_column(u'fadles_house', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Product.additional_info'
        db.alter_column(u'fadles_product', 'additional_info', self.gf('tinymce.models.HTMLField')())

    models = {
        u'fadles.house': {
            'Meta': {'object_name': 'House'},
            'description': ('ckeditor.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'preview': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        },
        u'fadles.houseimage': {
            'Meta': {'object_name': 'HouseImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['fadles.House']"})
        },
        u'fadles.product': {
            'Meta': {'object_name': 'Product'},
            'additional_info': ('ckeditor.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_popular': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'preview': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'start_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'fadles.productcertificate': {
            'Meta': {'object_name': 'ProductCertificate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'certificates'", 'to': u"orm['fadles.Product']"})
        },
        u'fadles.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['fadles.Product']"})
        }
    }

    complete_apps = ['fadles']