from django.conf.urls import url
from . import views


urlpatterns = [
	
	url('about', views.about, name='blog-about'),
 url('', views.home,name='blog-home'),


]