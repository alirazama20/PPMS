from django.db import models

from base.models import BaseModel
# Create your models here.

class MeterReading(BaseModel):
    date = models.DateTimeField(null=True)
    unit_one_current = models.FloatField(default=0,null=True,)
    unit_one_previous = models.FloatField(default=0,null=True, )
    unit_two_current = models.FloatField(default=0,null=True,)
    unit_two_previous = models.FloatField(default=0,null=True, )
    unit_three_current = models.FloatField(default=0,null=True, )
    unit_three_previous = models.FloatField(default=0,null=True, )
    unit_four_current = models.FloatField(default=0,null=True, )
    unit_four_previous = models.FloatField(default=0,null=True, )
    unit_five_current = models.FloatField(default=0,null=True, )
    unit_five_previous = models.FloatField(default=0,null=True, )
    unit_six_current = models.FloatField(default=0,null=True, )
    unit_six_previous = models.FloatField(default=0,null=True, )

    unit_one_equal = models.FloatField(default=0, null=True, )
    unit_two_equal = models.FloatField(default=0, null=True, )
    unit_three_equal = models.FloatField(default=0, null=True, )
    unit_four_equal = models.FloatField(default=0,null=True, )
    unit_five_equal = models.FloatField(default=0,null=True, )
    unit_six_equal = models.FloatField(default=0,null=True, )


    total_diesel = models.FloatField(default=0,null=True, )
    diesel_rate = models.FloatField(default=119.10, null=True, )
    diesel_Rs = models.FloatField(default=0, null=True, )

    total_petrol = models.FloatField(default=0,null=True, )
    petrol_rate = models.FloatField(default=122.40, null=True, )
    petrol_Rs = models.FloatField(default=0, null=True, )

    test_diesel = models.FloatField(default=0, null=True, )
    testDie_rate = models.FloatField(default=119.10, null=True, )
    testDie_Rs = models.FloatField(default=0, null=True, )

    test_petrol = models.FloatField(default=0, null=True, )
    testPet_rate = models.FloatField(default=122.40, null=True, )
    testPet_Rs = models.FloatField(default=0, null=True, )

    credit_diesel = models.FloatField(default=0, null=True, )
    crdie_rate = models.FloatField(default=119.10, null=True, )
    crdie_Rs = models.FloatField(default=0, null=True, )

    credit_petrol = models.FloatField(default=0, null=True, )
    crPet_rate = models.FloatField(default=122.40, null=True, )
    crPet_Rs = models.FloatField(default=0, null=True, )

    cash_diesel = models.FloatField(default=0, null=True, )
    cashDie_rate = models.FloatField(default=119.10, null=True, )
    cashDie_Rs = models.FloatField(default=0, null=True, )

    cash_petrol = models.FloatField(default=0, null=True, )
    cashPet_rate = models.FloatField(default=122.40, null=True, )
    cashPet_Rs = models.FloatField(default=0, null=True, )

    dunit_one_current = models.FloatField(default=0, null=True, )
    dunit_one_previous = models.FloatField(default=0, null=True, )
    dunit_two_current = models.FloatField(default=0, null=True, )
    dunit_two_previous = models.FloatField(default=0, null=True, )
    dunit_three_current = models.FloatField(default=0, null=True, )
    dunit_three_previous = models.FloatField(default=0, null=True, )
    dunit_four_current = models.FloatField(default=0, null=True, )
    dunit_four_previous = models.FloatField(default=0, null=True, )
    dunit_five_current = models.FloatField(default=0, null=True, )
    dunit_five_previous = models.FloatField(default=0, null=True, )
    dunit_six_current = models.FloatField(default=0, null=True, )
    dunit_six_previous = models.FloatField(default=0, null=True, )

    dunit_one_equal = models.FloatField(default=0, null=True, )
    dunit_two_equal = models.FloatField(default=0, null=True, )
    dunit_three_equal = models.FloatField(default=0, null=True, )
    dunit_four_equal = models.FloatField(default=0, null=True, )
    dunit_five_equal = models.FloatField(default=0, null=True, )
    dunit_six_equal = models.FloatField(default=0, null=True, )

    note = models.CharField(max_length=200, null=True,blank=True)


