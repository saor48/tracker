from django.db import models
from issues.models import Issue
from django.db.models.signals import post_save
from django.dispatch import receiver

class Comments(models.Model):
    issue = models.OneToOneField(Issue, on_delete=models.CASCADE, default="")
    commentary = models.TextField(max_length=5000, blank=True)
    text_length = models.CharField(max_length=254, default='')
    
    
@receiver(post_save, sender=Issue)
def create_issue_comments(sender, instance, created, **kwargs):
    if created:
        Comments.objects.create(issue=instance)

@receiver(post_save, sender=Issue)
def save_issue_comments(sender, instance, **kwargs):
    instance.comments.save()
