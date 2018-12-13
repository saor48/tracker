from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    
    features = forms.CharField(label="Voted Features")
    bugs = forms.CharField(label="Voted Bugs")
    paid_features = forms.CharField(label="Paid Features")
    
    class Meta:
        model = Profile
        fields = ['bugs','features', 'paid_features', 'latest_activity_date']