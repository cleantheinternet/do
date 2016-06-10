from django.contrib import admin
from .models import Campaign, PublisherCampaign, Finance

admin.site.register(Campaign)
admin.site.register(PublisherCampaign)
admin.site.register(Finance)
