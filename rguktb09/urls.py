from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rguktb09.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$','Students.views.home'),
    (r'^register/','Students.views.Register'),
    (r'^student$','Students.views.GetId'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)