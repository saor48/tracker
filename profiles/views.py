#profiles
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def get_profile(request):
    profile_form = ProfileForm(instance=request.user.profile)
    instance=request.user.profile
    feature_list=instance.features
    paid=instance.paid_features
    features = []
    for item in feature_list:
        if item.isdigit() and item not in paid:
            features.append(item)
    return render(request, 'profileprofile.html', {'profile_form': profile_form, 'features': features})

    
def update_profile(request):
    ###############update here######## but for vote ...done in issues!
    
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profileprofile.html', {'profile_form': profile_form})
    