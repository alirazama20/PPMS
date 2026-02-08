from django.db import models

# Create your models here.
from base.models import BaseModel
from master.models import Commission, Vechile, Item


class Sale(BaseModel):
    InvType = (
        ('CASH', 'CASH'),
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )
    Catagery = (
        ('Nil', 'Nil'),
        ('Bill Paid', 'Bill Paid'),
    )
    created_date = models.DateTimeField(null=True)
    date = models.DateTimeField(auto_now_add=False , auto_now = False ,null=True)
    invoiceType = models.CharField(default='Credit',max_length=10, null=True, choices=InvType)
    catagery = models.CharField(default='Nil',max_length=10, null=True, choices=Catagery)
    invoiceNo = models.CharField(default='nil', max_length=20, null=True)
    name = models.CharField(default='nil',max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True,blank=True)
    account = models.ForeignKey(Commission, on_delete=models.CASCADE, null=True)
    vechile = models.ForeignKey(Vechile, on_delete=models.CASCADE, null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0, null=True)
    saleprice = models.FloatField(default=273,null=True)
    purchase = models.FloatField(default=266.09, null=True)
    totalAmount = models.FloatField(default=0,null=True)
    paidAmount = models.FloatField(default=0,null=True)
    remainingAmount = models.FloatField(default=0,null=True)
    note = models.CharField(max_length=200, null=True,blank=True)
    profit = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.account) + ' ' + str(self.vechile)+''+str(self.item_name)+''+str(self.quantity)


class TyreSale(BaseModel):
    InvType = (
        ('CASH', 'CASH'),
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )
    Catagery = (
        ('Nil', 'Nil'),
        ('Bill Paid', 'Bill Paid'),
    )
    created_date = models.DateTimeField(null=True)
    date = models.DateTimeField(null=True)
    invoiceType = models.CharField(max_length=10, null=True, choices=InvType)
    catagery = models.CharField(max_length=10, null=True, choices=Catagery)
    invoiceNo = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True,blank=True)
    account = models.ForeignKey(Commission, on_delete=models.CASCADE, null=True)
    vechile = models.ForeignKey(Vechile, on_delete=models.CASCADE, null=True)
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0, null=True)
    saleprice = models.FloatField(default=0,null=True)
    purchase = models.FloatField(default=0, null=True)
    totalAmount = models.FloatField(default=0,null=True)
    paidAmount = models.FloatField(default=0,null=True)
    remainingAmount = models.FloatField(default=0,null=True)
    note = models.CharField(max_length=20, null=True,blank=True)
    profit = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.account) + ' ' + str(self.vechile)+''+str(self.item_name)+''+str(self.quantity)
