  from django.conf.urls import url
  from . import views           # This line is new!
  urlpatterns = [
    url(r'^$', views.index), 
    url(r'^/$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create)
	url(r'^show/(?p<id>\d+)/$', views.show)
	url(r'^edit/(?p<id>\d+)/$', views.edit)
	url(r'^destroy/(?p<id>\d+)/$', views.destroy)  
  ]
