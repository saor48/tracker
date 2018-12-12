#graphs
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from issues.models import Issue
from datetime import date as Date
from pprint import pprint

#get issues, 
#query = Issue.objects.all()
#query = Issue.objects.get(pk=issue_id)
#organise by dates
#send to file 
# d3

def graph(request):
    # calculate days between status dates and  make averages.  
    issued = 0
    accepted = 0
    started = 0
    completed = 0
    accepted_delays = 0
    started_delays = 0
    completed_delays = 0
    
    issues = Issue.objects.all()
    for issue in issues:
        accepted_delay = 0
        started_delay = 0
        completed_delay = 0
        issued += 1
        if issue.date_completed != None:
            completed += 1
            completed_delay = (issue.date_completed - issue.date_started).days
            started += 1
            started_delay = (issue.date_started - issue.date_accepted).days
            accepted += 1
            accepted_delay = (issue.date_accepted - issue.date_issued).days
        elif issue.date_started != None:
            started += 1
            started_delay = (issue.date_started - issue.date_accepted).days
            accepted += 1
            accepted_delay = (issue.date_accepted - issue.date_issued).days
        elif issue.date_accepted != None:
            accepted += 1
            accepted_delay = (issue.date_accepted - issue.date_issued).days
        accepted_delays += accepted_delay
        started_delays += started_delay
        completed_delays += completed_delay
    
    status = [issued,accepted,started,completed] 
    delays = [accepted_delays,started_delays,completed_delays]
    if accepted == 0:       #avoid division by 0
        accepted = 1
    if started == 0:
        started = 1
    if completed == 0:
        completed = 1
    averages = [accepted_delays/accepted,started_delays/started,completed_delays/completed]
    jav = [{"average":accepted_delays/accepted, "name":"accepted"},
            {"average":started_delays/started, "name":"started"},
            {"average":completed_delays/completed, "name":"completed"}]
        
    return render(request, "graphs.html", {"status":status, "delays": delays, "averages":averages, "jav":jav})
    
    