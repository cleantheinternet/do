from django import forms
from django.contrib.auth.models import User
from dashboard.models import Campaign


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'links', 'suggestion', 'views', 'duration']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
