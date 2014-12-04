from django.conf.urls import patterns, url
from bootstrappractice import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='bootstrappractice/index.html')),
    
)