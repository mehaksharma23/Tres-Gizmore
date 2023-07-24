from django.db import models

# Create your models here.

class Userinfo(models.Model):
    fullname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    userpassword = models.CharField(max_length=100, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    appleuserid = models.CharField(db_column='appleUserId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    istemporarypwd = models.IntegerField(db_column='istemporaryPwd', blank=True, null=True)  # Field name made lowercase.
    branchid = models.BigIntegerField(blank=True, null=True)
    companyid = models.BigIntegerField(blank=True, null=True)
    modificationdate = models.DateTimeField(blank=True, null=True)
    employeecode = models.CharField(db_column='EmployeeCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    latestreadingtime = models.DateTimeField(db_column='latestreadingTime', blank=True, null=True)  # Field name made lowercase.
    transferred_emailid = models.CharField(max_length=100, blank=True, null=True)
    transferred_appleuserid = models.CharField(max_length=100, blank=True, null=True)
    lasthealthriskrating = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(db_column='Designation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.BigIntegerField(db_column='MobileNo', blank=True, null=True)  # Field name made lowercase.
    deviceos = models.CharField(max_length=100, blank=True, null=True)
    devicetype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'