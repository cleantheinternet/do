from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^ccampaign/(?P<campaign_id>[0-9]+)$', views.ccampaign, name='ccampaign'),
    url(r'^pcampaign/(?P<publishercampaign_id>[0-9]+)$', views.pcampaign, name='pcampaign'),
    url(r'^create_campaign/$', views.create_campaign, name='create_campaign'),
    url(r'^finance/$', views.finance, name='finance'),
]
