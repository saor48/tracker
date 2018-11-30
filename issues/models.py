from django.db import models

class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    comment = models.TextField(blank=True, default='')
    category = models.CharField(max_length=10, default='bug')
    date_issued = models.DateField(auto_now_add=True) 
    date_accepted = models.DateField(blank=True, null=True)
    date_started = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    #image = models.ImageField(upload_to='images')
    
    def __str__(self):
        
        return self.name
