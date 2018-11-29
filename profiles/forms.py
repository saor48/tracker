from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('features', 'bugs','paid_features', 'latest_activity_date')