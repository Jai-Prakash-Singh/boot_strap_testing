from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blongo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blogapp/', include('blogapp.urls', namespace="blogapp")),

    url(r'^admin/', include(admin.site.urls)),
)
