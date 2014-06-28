# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductCertificate'
        db.create_table(u'fadles_productcertificate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='certificates', to=orm['fadles.Product'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'fadles', ['ProductCertificate'])

        # Adding field 'Product.preview'
        db.add_column(u'fadles_product', 'preview',
                      self.gf('sorl.thumbnail.fields.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Product.is_popular'
        db.add_column(u'fadles_product', 'is_popular',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Product.start_price'
        db.add_column(u'fadles_product', 'start_price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Product.unit'
        db.add_column(u'fadles_product', 'unit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16),
                      keep_default=False)

        # Adding field 'Product.additional_info'
        db.add_column(u'fadles_product', 'additional_info',
                      self.gf('tinymce.models.HTMLField')(default=''),
                      keep_default=False)


        # Changing field 'Product.description'
        db.alter_column(u'fadles_product', 'description', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'ProductCertificate'
        db.delete_table(u'fadles_productcertificate')

        # Deleting field 'Product.preview'
        db.delete_column(u'fadles_product', 'preview')

        # Deleting field 'Product.is_popular'
        db.delete_column(u'fadles_product', 'is_popular')

        # Deleting field 'Product.start_price'
        db.delete_column(u'fadles_product', 'start_price')

        # Deleting field 'Product.unit'
        db.delete_column(u'fadles_product', 'unit')

        # Deleting field 'Product.additional_info'
        db.delete_column(u'fadles_product', 'additional_info')


        # Changing field 'Product.description'
        db.alter_column(u'fadles_product', 'description', self.gf('django.db.models.fields.TextField')(max_length=2048))

    models = {
        u'fadles.product': {
            'Meta': {'object_name': 'Product'},
            'additional_info': ('tinymce.models.HTMLField', [], {}),
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