from django.db import models

# Create your models here.

class cfa_wl(models.Model):

    PHONE_NO = models.CharField(max_length=12)
    NAME = models.CharField(max_length=100)
    HOUSE_NO = models.CharField(max_length=50)
    VILLAGE_NAME = models.CharField(max_length=100)
    ADDITIONAL_DETAILS = models.CharField(max_length=50)
    CITY = models.CharField(max_length=50)
    PIN_CODE = models.CharField(max_length=6)
    SWITCH_CODE = models.CharField(max_length=20)
    NE = models.CharField(max_length=20)
    PORT_CARD_SLOT = models.CharField(max_length=5)
    VERTICAL = models.CharField(max_length=20)
    PILLAR_IN = models.CharField(max_length=30)
    PILLAR_OUT = models.CharField(max_length=30)
    DP_NO = models.CharField(max_length=30)
    LINEMAN_CODE = models.CharField(max_length=30)
    JTO_CODE = models.CharField(max_length=20)
    BB_FLAG = models.CharField(max_length=2)
    BB_PLAN = models.CharField(max_length=100)
    LL_PLAN = models.CharField(max_length=50)
    OS_AMOUNT = models.CharField(max_length=10)
    OPERATING_STATUS = models.CharField(max_length=20)
    MOBILE_NO = models.CharField(max_length=10)
    EMAIL_ID = models.CharField(max_length=50)

class cfa_bb(models.Model):
    
    SSA = models.CharField(max_length=20)
    EXCHANGE_CODE = models.CharField(max_length=10)
    PHONE_NO = models.CharField(max_length=12)
    USER_ID = models.CharField(max_length=30)
    NW_TYPE = models.CharField(max_length=5)
    MODEM_TYPE = models.CharField(max_length=20)
    MODEM_ACQ_TYPE = models.CharField(max_length=20)
    DSLAM_IP = models.CharField(max_length=20)
    INNER_VLAN = models.CharField(max_length=5)
    OUTER_VLAN = models.CharField(max_length=5)



