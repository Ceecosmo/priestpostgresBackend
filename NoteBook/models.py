from django.db import models

# Create your models here.


class Notebook(models.Model):
    name=models.CharField(max_length=500)
    subject=models.CharField(max_length=500)
    Write_Your_Note=models.TextField(max_length=1000000,null=True,blank=True)
    #create variable 'created_at' for date and time for the message sent
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
    
       return  "Name: "+ self.name +",  Subject: "+ self.subject


