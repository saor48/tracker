#issues
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Issue
from datetime import date as Date
from .forms import CreateIssueForm, EditIssueForm, CommentForm
from pprint import pprint

#----------------------------------Functions x2--------------------------------------#
def get_issue(issue_id):
    query = Issue.objects.get(pk=issue_id)
    return query

def update_profile(user_id,**kwargs):
    user = User.objects.get(pk=user_id)
    user.profile.latest_activity_date = Date.today()
    if kwargs is not None:
        for key in kwargs:
            value = str(kwargs[key]) + ","
            if key == 'bug':
                user.profile.bugs += value
            if key == 'feature':
                user.profile.features += value
            if key == 'paid':
                user.profile.paid_features += value
    user.save()

    
# line def-------------------------------Views x8--------------------------------------#
# 42 issues --------------- displays all issues
# 53 vote ----------------- adds issue id to profile bug/feature voted field
# 68 bug ------------------ create an issue
# 94 edit_issue ----------- form to edit an issue
# 114 update_issue -------- update an issue
# 129 delete_issue -------- delete an issue
# 136 make_comment -------- form to enter a comment
# 148 update_comment ------ save comment to db

@login_required
def issues(request):
    query = Issue.objects.all()
    user = User.objects.get(pk=request.user.id)
    user.profile.latest_activity_date = Date.today()
    #now.strftime("%Y-%m-%d")
    pprint(vars(user.profile)) 
    pprint(vars(user)) 
    user.save()
    return render(request, 'issues.html', { 'issues' : query } )


def vote(request):
    issue_id = request.POST.get('issue_id')
    query = get_issue(issue_id)
    user_id = request.user.id
    instance=request.user.profile
    features=instance.features.split(",")
    bugs=instance.bugs.split(",")
    if str(query.id) not in features and str(query.id) not in bugs:
        kwargs = {query.category : query.id}
        update_profile(user_id, **kwargs)
    else:
        messages.error(request, "You have already voted on this issue")
    return redirect(reverse('get_profile'))

    
def bug(request):
    if request.method == 'POST':
        form = CreateIssueForm(request.POST)
        if form.is_valid():
            query = Issue(
                    name = form.cleaned_data['name'],
                    owned_by = request.user,
                    description = form.cleaned_data['description'],
                    comment = "",
                    category = form.cleaned_data['category'],
                    date_issued = Date.today, 
                    date_accepted = None,
                    date_started = None,
                    date_completed = None,
                    price = None,
                    )
            query.save()
            user_id = request.user.id
            kwargs = {query.category : query.id}
            update_profile(user_id, **kwargs)
            return redirect(reverse('issues'))
    else:
        form = CreateIssueForm()
    return render(request, 'bug.html', {'bugform': form})
    
    
def edit_issue(request):
    user_id = request.user.id
    issue_id = request.POST.get('issue_id')
    issue = get_issue(issue_id)
    if user_id == issue.owned_by.id:
        form = EditIssueForm(initial={
                    'id' : issue_id,
                    'name' : issue.name,
                    'description' : issue.description,
                    'category' : issue.category,
                    'date_accepted' : issue.date_accepted,
                    'date_started' : issue.date_started,
                    'date_completed' : issue.date_completed
                    })
    else:
        messages.error(request, "-- Action Not Allowed: --> Issues can only be edited and deleted by creator <--")
        return redirect(reverse("issues"))
    return render(request, 'editIssue.html', {'edit_issue_form': form, 'issue_id':issue_id })


def update_issue(request):
    if request.method == 'POST':
        form = EditIssueForm(request.POST)
        if form.is_valid():
            issue=Issue.objects.filter(pk=form.cleaned_data['id'])
            issue.update(
                    date_accepted = form.cleaned_data['date_accepted'],
                    date_started = form.cleaned_data['date_started'],
                    date_completed = form.cleaned_data['date_completed'],
                    )
        else:
            return render(request, 'editIssue.html', {'edit_issue_form': form, 'error_message': 'Incorrect entry - Try again'})
    return redirect(reverse('issues'))
            

def delete_issue(request):
    issue_id = request.POST.get('issue_id')
    query = Issue.objects.get(pk=issue_id)
    issue = query.delete()
    return redirect(reverse('issues'))       


def make_comment(request):
    issue_id = request.POST.get('issue_id')
    issue = get_issue(issue_id)
    form = CommentForm(initial={
                    'id' : issue_id,
                    'name' : issue.name,
                    'description' : issue.description,
                    'comment' : ""
                    })
    return render(request, 'comment.html', {'comment_form': form, 'issue_id':issue_id })


def update_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['comment'] != '':
                issue=Issue.objects.get(pk=form.cleaned_data['id'])
                text= str(form.cleaned_data['comment'])
                user = str(request.user)
                date = str(Date.today())
                commentary = { "text":text, "author":user, "date":date }
                separator = "(}{)"
                issue.comments.commentary += str(commentary) + separator 
                issue.comments.text_length += str(len(commentary)) + ","
                issue.save()
        else:
            messages.error(request, "Unable to process comment")
            return redirect(reverse('make_comment'))
    return redirect(reverse('issues'))
    
    