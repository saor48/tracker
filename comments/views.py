#comments
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import Issue
import json

def commentary(request):
    issue_id = request.POST.get('issue_id')
    instance = Issue.objects.get(pk=issue_id)

    separator = "(}{)"
    comment_list=instance.comments.commentary.split(separator)
   
    commentary = []
    for i in range(0, len(comment_list)-1):
        commentary.append(json.loads(comment_list[i].replace("'", "\"")))
    
    return render(request, 'comments.html', {'commentary':commentary})    
        
        
        
        