from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=30,null=True,blank=True)
    subject=models.CharField(max_length=500)
    message=models.TextField()
    #create variable 'created_at' for date and time for the message sent
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
    
       return  "Full Name: "+ self.name +",  Email: "+ self.email