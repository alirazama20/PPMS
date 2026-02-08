from django.db import models
from base.models import BaseModel
from master.models import Expense

# Create your models here.

class ExpenseDetail(BaseModel):
    EXPTYPE = (
        ('CASH', 'CASH'),
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    )
    exp_type = models.CharField(max_length=10  , null=True, choices=EXPTYPE)
    exp_name = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0,null=True)
    date = models.DateTimeField(null=True)
    note = models.CharField(max_length=300, null=True,blank=True)
    def __str__(self):
        return str(self.exp_name) + ' ' + str(self.amount)

