from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Issue
from datetime import date as Date
from .forms import CreateIssueForm, EditIssueForm
from pprint import pprint
#now.strftime("%Y-%m-%d %H:%M")


#----------------------------------Functions-----------------------------------------#
def get_issue(issue_id):
    query = Issue.objects.get(pk=issue_id)
    print("getissue--------", query)
    return query

def update_profile(user_id,**kwargs):
    print("user-",user_id)
    user = User.objects.get(pk=user_id)
    user.profile.latest_activity_date = Date.today()
    #now.strftime("%Y-%m-%d")
    if kwargs is not None:
        print("kws==", kwargs)
        for key in kwargs:
            value = str(kwargs[key])
            if key == 'bug':
                user.profile.bugs += ',' + value
            if key == 'feature':
                user.profile.features += ',' + value
            if key == 'paid':
                user.profile.paid_features += ',' + value
    print("user-", user)
    pprint(vars(user))
    pprint(vars(user.profile))
    user.save()
    
#-----------------------------------Views----------------------------------------#

@login_required
def issues(request):
    query = Issue.objects.all()
    current_user = request.user
    print("user-",current_user.id)
    user = User.objects.get(pk=current_user.id)
    user.profile.latest_activity_date = Date.today()
    #now.strftime("%Y-%m-%d")
    result='' # put result in session/?
    if result:
        # set features, bugs, paid_features
        print("result", result)
    print("user-", user)
    pprint(vars(user))
    pprint(vars(user.profile))
    user.save()
    return render(request, 'issues.html', { 'issues' : query } )


def vote(request):
    issue_id = request.POST.get('issue_id')
    query = get_issue(issue_id)
    user_id = request.user.id
    kwargs = {query.category : query.id}
    print("resultvote=", user_id," -q-",query.id)
    update_profile(user_id, **kwargs)
    return redirect(reverse('issues'))

    
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
            print("form---", form)
            query.save()
            
            user_id = request.user.id
            kwargs = {query.category : query.id}
            print("result=", user_id," -q-",query.id)
            update_profile(user_id, **kwargs)
            return redirect(reverse('issues'))
    else:
        form = CreateIssueForm()
    print("form--------", form)        
    return render(request, 'bug.html', {'bugform': form})
    
    
def edit_issue(request):
    
    issue_id = request.POST.get('issue_id')
    print("edit-rfid--", issue_id)
    issue = get_issue(issue_id)
    print("edit-issue--", issue)
    
            
    form = EditIssueForm(initial={
                    'id' : issue_id,
                    'name' : issue.name,
                    'description' : issue.description,
                    'comment' : issue.comment,
                    'category' : issue.category,
                    'date_accepted' : issue.date_accepted,
                    'date_started' : issue.date_started,
                    'date_completed' : issue.date_completed
                    })

    print("edit--", form)      
    return render(request, 'editIssue.html', {'edit_issue_form': form})

    
def update_issue(request):
    if request.method == 'POST':
        form = EditIssueForm(request.POST)
        print("update----",form.data['name'])
        print("upform---",form)
        if form.is_valid():
            #form.save()
            Issue.objects.filter(pk=form.cleaned_data['id']).update(
                    comment = form.cleaned_data['comment'],
                    date_accepted = form.cleaned_data['date_accepted'],
                    date_started = form.cleaned_data['date_started'],
                    date_completed = form.cleaned_data['date_completed'],
                    )
        else:
            return render(request, 'editIssue.html', {'edit_issue_form': form, 'error_message': 'Incorrect entry - Try again'})
    return redirect(reverse('issues'))
            

def delete_issue(request):
    
    issue_id = request.POST.get('issue_id')
    print("delete-rfid--", issue_id)
    query = Issue.objects.get(pk=issue_id)
    issue = query.delete()
    print("delete-issue--", issue)
    return redirect(reverse('issues'))       
            