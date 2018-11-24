from django.shortcuts import render, redirect, reverse
from .models import Issue
from datetime import date as Date
from .forms import CreateIssueForm, EditIssueForm


def issues(request):
    issues = Issue.objects.all()
    extras = ['date_accepted','date_started', 'date_completed', 'price']
 
    print("is--", issues)

    return render(request, 'issues.html', { 'issues' : issues } )
    
    
def bug(request):
    
    if request.method == 'POST':
        form = CreateIssueForm(request.POST)
        if form.is_valid():
            query = Issue(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    comment = "",
                    category = form.cleaned_data['category'],
                    date_issued = Date.today, 
                    date_accepted = None,
                    date_started = None,
                    date_completed = None,
                    price = None,
                    )
            print("query---", query)
            query.save()
            return redirect(reverse('issues'))
    else:
        form = CreateIssueForm()
    print("form--------", form)        
    return render(request, 'bug.html', {'form': form})
    
    
    