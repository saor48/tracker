from django import forms
from .models import Issue
#ChoiceField(choices=CATEGORY_CHOICES)

class CreateIssueForm(forms.ModelForm):
    CATEGORY_CHOICES = [('bug', 'Bug'), ('feature', 'Feature')]
    name = forms.CharField(label='Name', max_length=254, required=True)
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    category = forms.ChoiceField(label='Category', choices=CATEGORY_CHOICES, required=True)
    class Meta:
        model = Issue
        fields = ['name','description','category']


class EditIssueForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    description = forms.CharField(label='Description', max_length=254, required=True)
    class Meta:
        model = Issue
        fields = ['id','name','description','category','date_accepted','date_started','date_completed']
        widgets = {
            'date_accepted': forms.DateInput(attrs={'class':'datepicker'}),
            'date_started': forms.DateInput(attrs={'class':'datepicker'}),
            'date_completed': forms.DateInput(attrs={'class':'datepicker'}),
        }

class CommentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    description = forms.CharField(label='Description', max_length=254, required=True)
    class Meta:
        model = Issue
        fields = ['id','name','description','comment']
    