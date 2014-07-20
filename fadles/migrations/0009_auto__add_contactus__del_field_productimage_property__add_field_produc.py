# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactUs'
        db.create_table(u'fadles_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fadles', ['ContactUs'])

        # Deleting field 'ProductImage.property'
        db.delete_column(u'fadles_productimage', 'property_id')

        # Adding field 'ProductImage.product'
        db.add_column(u'fadles_productimage', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='images', to=orm['fadles.Product']),
                      keep_default=False)

        # Deleting field 'ProductCertificate.property'
        db.delete_column(u'fadles_productcertificate', 'property_id')

        # Adding field 'ProductCertificate.product'
        db.add_column(u'fadles_productcertificate', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='certificates', to=orm['fadles.Product']),
                      keep_default=False)

        # Deleting field 'HouseImage.property'
        db.delete_column(u'fadles_houseimage', 'property_id')

        # Adding field 'HouseImage.product'
        db.add_column(u'fadles_houseimage', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='images', to=orm['fadles.House']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ContactUs'
        db.delete_table(u'fadles_contactus')

        # Adding field 'ProductImage.property'
        db.add_column(u'fadles_productimage', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='images', to=orm['fadles.Product']),
                      keep_default=False)

        # Deleting field 'ProductImage.product'
        db.delete_column(u'fadles_productimage', 'product_id')

        # Adding field 'ProductCertificate.property'
        db.add_column(u'fadles_productcertificate', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='certificates', to=orm['fadles.Product']),
                      keep_default=False)

        # Deleting field 'ProductCertificate.product'
        db.delete_column(u'fadles_productcertificate', 'product_id')

        # Adding field 'HouseImage.property'
        db.add_column(u'fadles_houseimage', 'property',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='images', to=orm['fadles.House']),
                      keep_default=False)

        # Deleting field 'HouseImage.product'
        db.delete_column(u'fadles_houseimage', 'product_id')


    models = {
        u'fadles.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
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
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['fadles.House']"})
        },
        u'fadles.popularproduct': {
            'Meta': {'object_name': 'PopularProduct'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'preview': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'populars'", 'to': u"orm['fadles.Product']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'start_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '16'})
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
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'certificates'", 'to': u"orm['fadles.Product']"})
        },
        u'fadles.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['fadles.Product']"})
        },
        u'fadles.producttable': {
            'Meta': {'object_name': 'ProductTable'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tables'", 'to': u"orm['fadles.Product']"}),
            'table': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'table_json': ('django.db.models.fields.TextField', [], {})
        },
        u'fadles.sale': {
            'Meta': {'object_name': 'Sale'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'preview': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sales'", 'to': u"orm['fadles.Product']"})
        }
    }

    complete_apps = ['fadles']