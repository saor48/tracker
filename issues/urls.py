from django.conf.urls import url
from .views import issues, bug, edit_issue, get_issue, update_issue, delete_issue, vote, make_comment, update_comment


urlpatterns = [
    url(r'^$', issues, name="issues"),
    url(r'^bug/', bug, name="bug"),
    url(r'^editIssue/', edit_issue, name="edit_issue"),
    url(r'^update/', update_issue, name="update_issue"),
    url(r'^delete/', delete_issue, name="delete_issue"),
    url(r'^vote/', vote, name="vote"),
    url(r'^comment/', make_comment, name="make_comment"),
    url(r'^comment_update/', update_comment, name="update_comment"),
]