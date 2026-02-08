from django.db import models

from base.models import BaseModel
# Create your models here.
class DailyStock(BaseModel):
    date = models.DateTimeField(null=True)
    dip_one_hsd = models.FloatField(default=0,null=True,)
    ltrs_one_hsd = models.FloatField(default=0, null=True, )
    diff_ltrs_one_hsd = models.FloatField(default=0, null=True, )
    status_one_hsd = models.FloatField(default=0, null=True, )
    stock_one_hsd = models.FloatField(default=0, null=True, )
    sale_one_hsd = models.FloatField(default=0, null=True, )
    rmg_one_hsd = models.FloatField(default=0, null=True, )

    dip_two_hsd = models.FloatField(default=0, null=True, )
    ltrs_two_hsd = models.FloatField(default=0, null=True, )
    diff_ltrs_two_hsd = models.FloatField(default=0, null=True, )
    status_two_hsd = models.FloatField(default=0, null=True, )
    stock_two_hsd = models.FloatField(default=0, null=True, )
    sale_two_hsd = models.FloatField(default=0, null=True, )
    rmg_two_hsd = models.FloatField(default=0, null=True, )

    dip_pmg = models.FloatField(default=0, null=True, )
    ltrs_pmg = models.FloatField(default=0, null=True, )
    diff_pmg = models.FloatField(default=0, null=True, )
    status_pmg = models.FloatField(default=0, null=True, )
    stock_pmg = models.FloatField(default=0, null=True, )
    sale_pmg = models.FloatField(default=0, null=True, )
    rmg_pmg = models.FloatField(default=0, null=True, )

    note = models.CharField(max_length=200, null=True,blank=True)







