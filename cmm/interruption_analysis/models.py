from django.db import models

# Create your models here.


class interruptions_table(models.Model):

    #id = models.IntegerField(primary_key='True')
    RPID = models.CharField(max_length=50)
    BTS_NAME = models.CharField(max_length=50)
    BTS_TRF_CAT = models.CharField(max_length=50)
    SSA = models.CharField(max_length=50)
    SDCA = models.CharField(max_length=50)
    CIRCLE = models.CharField(max_length=50)
    MAKE = models.CharField(max_length=50)
    TECH = models.CharField(max_length=50)
    SITE_TYPE = models.CharField(max_length=50)
    DOWN_DATE = models.CharField(max_length=50)
    DOWN_TIME = models.CharField(max_length=50)
    CLEARED_DATE = models.CharField(max_length=50)
    CLEARED_TIME = models.CharField(max_length=50)
    REASON = models.CharField(max_length=100)
    DURATION = models.FloatField()


