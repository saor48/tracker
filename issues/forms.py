from django import forms
from .models import Issue

class CreateIssueForm(forms.Form):
    
    CATEGORY_CHOICES = ['Bug', 'Feature'] 
    
    name = forms.CharField(label='Name', max_length=254, required=True)
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    category = forms.CharField(label='Category', max_length=254, required=True)
    #ChoiceField(choices=CATEGORY_CHOICES )
    


class EditIssueForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    class Meta:
        model = Issue
        fields = ('id', 'name', 'comment','category', 'date_accepted', 'date_started', 'date_completed')
        
    