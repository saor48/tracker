#profiles
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def get_profile(request):
    #query = Profile.objects.all()
    #user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profileprofile.html', {'profile_form': profile_form})

    
def update_profile(request):
    ###############update here######## but for vote ...done in issues!
    
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profileprofile.html', {'profile_form': profile_form})
    