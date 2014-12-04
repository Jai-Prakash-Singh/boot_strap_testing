from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
     #url(r'^(/)?$', RedirectView.as_view(url='/chats/')),
     #url(r'^chats/', include('chat.urls')),
     url(r'^(/)?$', RedirectView.as_view(url='/polls/')),
     url(r'^polls/', include('polls.urls', namespace="polls")),
     url(r'^bootprac/', include('bootstrappractice.urls', namespace="bootprac")),
     url(r'^admin/', include(admin.site.urls)),
)


