from django.db import models
from base.models import BaseModel
from master.models import Dealer,Item

# Create your models here.

class Purchase(BaseModel):

    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True)
    invoice_No = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0,null=True,)
    rate = models.FloatField(default=0, null=True, )
    total = models.FloatField(default=0,null=True)
    paid = models.FloatField(default=0,null=True)
    remaining = models.FloatField(default=0,null=True)
    note = models.CharField(max_length=1000, null=True,blank=True)

    def __str__(self):
        return str(self.product)