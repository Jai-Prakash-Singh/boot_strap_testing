from django.conf.urls import patterns, url
from login_app import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
	url(r'^log/$', TemplateView.as_view(template_name='login_app/login.html')),
    url(r'^reg/$', TemplateView.as_view(template_name='login_app/register.html')),
    
)