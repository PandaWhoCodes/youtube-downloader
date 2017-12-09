from django.conf.urls import include, url
from .views import home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [url(r'^$', home, name='home'),
               # Uncomment the admin/doc line below to enable admin documentation:
               # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

               # Uncomment the next line to enable the admin:
               # url(r'^admin/', include(admin.site.urls)),
               ]
# urlpatterns += patterns('',
#                         (
#                         r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#                         )
