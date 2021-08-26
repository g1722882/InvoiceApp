from django.db import models
import datetime
# Create your models here.
class Invoice(models.Model):
    #customer = models.CharField(max_length=100)
    buyer_name = models.CharField(max_length=30, default='')
    seller_name = models.CharField(max_length=30, default='')
    seller_billing_address = models.TextField(null=False, blank=True)
    buyer_billing_address = models.TextField(null=False, blank=True)    
    date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.buyer_name)
        return str(self.seller_name)
    
    def get_status(self):
        return self.status

    def save(self, *args, **kwargs):
        if not self.id:             
            self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)
   