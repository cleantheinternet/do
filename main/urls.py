from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publisher/$', views.publishers, name='publishers'),
    url(r'^companies/$', views.companies, name='companies'),
    url(r'^about/$', views.about, name='about'),
]
