# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'fadles_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
            ('preview', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('review', self.gf('django.db.models.fields.TextField')()),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('moderated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'fadles', ['Review'])

        # Deleting field 'ContactUs.phone'
        db.delete_column(u'fadles_contactus', 'phone')

        # Deleting field 'ContactUs.email'
        db.delete_column(u'fadles_contactus', 'email')

        # Adding field 'ContactUs.email_or_phone'
        db.add_column(u'fadles_contactus', 'email_or_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'fadles_review')

        # Adding field 'ContactUs.phone'
        db.add_column(u'fadles_contactus', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256),
                      keep_default=False)

        # Adding field 'ContactUs.email'
        db.add_column(u'fadles_contactus', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=256),
                      keep_default=False)

        # Deleting field 'ContactUs.email_or_phone'
        db.delete_column(u'fadles_contactus', 'email_or_phone')


    models = {
        u'fadles.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_or_phone': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
        u'fadles.review': {
            'Meta': {'object_name': 'Review'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'preview': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'review': ('django.db.models.fields.TextField', [], {})
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