from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fadles.views.home_view', name='home'),
    url(r'^catalog/$', 'fadles.views.catalog_view', name='catalog'),
    url(r'^product/(?P<product_id>\d+)/$', 'fadles.views.product_view', name='product'),
    url(r'^houses/$', 'fadles.views.catalog_houses_view', name='houses'),
    url(r'^house/(?P<house_id>\d+)/$', 'fadles.views.house_view', name='house'),
    url(r'^reviews/$', 'fadles.views.review_view', name='review'),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('fadles.ckeditor_urls')),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Flatpages
urlpatterns += patterns('',
    url(r'^contacts/', include('django.contrib.flatpages.urls'), name='contact_us'),
    url(r'^partners/', include('django.contrib.flatpages.urls'), name='partners'),
    url(r'^about/', include('django.contrib.flatpages.urls'), name='about'),
)