from django.conf.urls import url, include
from .views import issues, bug, edit_issue, get_issue, update_issue, delete_issue, vote


urlpatterns = [
    url(r'^$', issues, name="issues"),
    url(r'^bug/', bug, name="bug"),
    url(r'^editIssue/', edit_issue, name="edit_issue"),
    url(r'^update/', update_issue, name="update_issue"),
    url(r'^delete/', delete_issue, name="delete_issue"),
    url(r'^vote/', vote, name="vote"),
]