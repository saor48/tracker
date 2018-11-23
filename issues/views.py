from django.shortcuts import render, redirect, reverse
from .models import Issue
from datetime import date as Date

def issues(request):
    issues = Issue.objects.all()
    extras = ['date_accepted','date_started', 'date_completed', 'price']
 
    print("is--", issues)

    return render(request, 'issues.html', { 'issues' : issues } )

def bug(request):
    
    query = Issue(
        name = "new issue",
        description = "created in views",
        comment = "",
        category = "bug",
        date_issued = Date.today, 
        date_accepted = None,
        date_started = None,
        date_completed = None,
        price = None,
        )
    
    if request.method == "POST":
        
        query.save()
        
        return redirect(reverse('issues'))
    
    return render(request, 'bug.html' )
    
    