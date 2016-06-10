from django.shortcuts import render, get_object_or_404
from .models import Campaign, PublisherCampaign, Finance
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import CampaignForm, UserForm


def create_campaign(request):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        form = CampaignForm(request.POST or None)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return render(request, 'dashboard/ccampaign.html', {'campaign': campaign})
        else:
            return render(request, 'dashboard/create_campaign.html', {'form': form})


def ccampaign(request, campaign_id):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        user = request.user
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        return render(request, 'dashboard/ccampaign.html', {'campaign': campaign, 'user': user})


def pcampaign(request, publishercampaign_id):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        user = request.user
        publishercampaign = get_object_or_404(PublisherCampaign, pk=publishercampaign_id)
        return render(request, 'dashboard/pcampaign.html', {'publishercampaign': publishercampaign, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'dashboard/login.html')
    else:
        user = request.user
        campaigns = Campaign.objects.filter(user=request.user)
        publishercampaigns = PublisherCampaign.objects.filter(user=request.user)
        return render(request, 'dashboard/index.html', {'campaigns': campaigns,
                                                        'publishercampaigns': publishercampaigns, 'user': user})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'dashboard/login.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                campaigns = Campaign.objects.filter(user=request.user)
                publishercampaigns = PublisherCampaign.objects.filter(user=request.user)
                return render(request, 'dashboard/index.html',
                              {'campaigns': campaigns, 'publishercampaigns': publishercampaigns})
            else:
                return render(request, 'dashboard/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dashboard/login.html', {'error_message': 'You entered wrong username/password. '
                                                                             'Remember username is not your email'})
    return render(request, 'dashboard/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                campaigns = Campaign.objects.filter(user=request.user)
                publishercampaigns = PublisherCampaign.objects.filter(user=request.user)
                return render(request, 'dashboard/index.html',
                              {'campaigns': campaigns, 'publishercampaigns': publishercampaigns})
            else:
                return render(request, 'dashboard/register.html', {'error_message':'You entered wrong details. '
                                                                                   'Try again'})
    return render(request, 'dashboard/register.html', {'form': form})

def finance(request):
    money = Finance.objects.all()
    return render(request, 'dashboard/finance.html', {'money': money})

