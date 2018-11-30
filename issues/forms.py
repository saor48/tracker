from django import forms
from .models import Issue
#ChoiceField(choices=CATEGORY_CHOICES )

class CreateIssueForm(forms.ModelForm):
    
    CATEGORY_CHOICES = ['Bug', 'Feature'] 
    
    name = forms.CharField(label='Name', max_length=254, required=True)
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    category = forms.CharField(label='Category', max_length=254, required=True)
    class Meta:
        model = Issue
        fields = ['name','description','category']


class EditIssueForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Issue
        fields = ['id','name','description','comment','category','date_accepted','date_started','date_completed']
        
    