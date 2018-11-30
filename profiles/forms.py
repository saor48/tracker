from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    
    features = forms.CharField(label="Features")
    bugs = forms.CharField()
    paid_features = forms.CharField(label="Paid")
    
    class Meta:
        model = Profile
        fields = ['bugs','features', 'paid_features', 'latest_activity_date']