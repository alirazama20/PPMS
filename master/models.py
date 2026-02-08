from django.db import models

from base.models import BaseModel

# Create your models here.

class Item(BaseModel):
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

class Dealer(BaseModel):
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

class Commission(BaseModel):
    name = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Expense(BaseModel):
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

class Employee(BaseModel):
    emp_name = models.CharField(max_length=20, null=True)
    salary = models.FloatField(null=True)
    perday = models.FloatField(null=True)
    def __str__(self):
        return self.emp_name

class Vechile(BaseModel):
    account = models.ForeignKey(Commission, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

class Rate(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

