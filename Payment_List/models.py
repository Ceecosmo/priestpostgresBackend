from django.db import models
import secrets 
from .paystack import PayStack


# Create your models here.


class Payment(models.Model):
    creditors_FullName=models.CharField(max_length=1000)
    amount = models.PositiveIntegerField(default=0.00)
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number=models.CharField(max_length=100)
    message=models.TextField(max_length=10000,null=True,blank=True)
    #create variable 'created_at' for date and time for the message sent
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"Creditor's Email: {self.email}, Amount Credited: {self.amount}"
        
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref: 
               self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self) -> int:
        return self.amount *100


    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
        return False     


