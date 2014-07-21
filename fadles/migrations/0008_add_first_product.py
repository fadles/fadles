# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.Product.objects.create(name=u'Very misterious player', pk=1)
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        print 'here'
        orm.Product.objects.get(pk=1).delete()
        "Write your backwards methods here."


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
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'certificates'", 'to': u"orm['fadles.Product']"})
        },
        u'fadles.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['fadles.Product']"})
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
    symmetrical = True
