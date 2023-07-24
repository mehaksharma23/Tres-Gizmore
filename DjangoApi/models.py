# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminuser(models.Model):
    adminid = models.BigAutoField(primary_key=True)
    companyid = models.BigIntegerField(blank=True, null=True)
    branchid = models.TextField(blank=True, null=True)
    firstname = models.CharField(max_length=155, blank=True, null=True)
    userpassword = models.CharField(max_length=105, blank=True, null=True)
    email = models.CharField(max_length=105, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    lastname = models.CharField(max_length=105, blank=True, null=True)
    phoneno = models.CharField(max_length=45, blank=True, null=True)
    adminusercol = models.CharField(max_length=45, blank=True, null=True)
    istemporarypwd = models.IntegerField(db_column='istemporaryPwd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminuser'


class Adminusertemp(models.Model):
    adminid = models.BigIntegerField()
    companyid = models.BigIntegerField(blank=True, null=True)
    branchid = models.TextField(blank=True, null=True)
    firstname = models.CharField(max_length=155, blank=True, null=True)
    userpassword = models.CharField(max_length=105, blank=True, null=True)
    email = models.CharField(max_length=105, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    lastname = models.CharField(max_length=105, blank=True, null=True)
    phoneno = models.CharField(max_length=45, blank=True, null=True)
    adminusercol = models.CharField(max_length=45, blank=True, null=True)
    istemporarypwd = models.IntegerField(db_column='istemporaryPwd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminusertemp'


class Apphistory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.BigIntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.CharField(db_column='ReleaseDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='AppVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ostype = models.CharField(db_column='OSType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    buildnumber = models.CharField(db_column='BuildNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isforcefullupdate = models.CharField(db_column='IsForcefullUpdate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uploadedby = models.BigIntegerField(db_column='UploadedBy', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apphistory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BadgeMaster(models.Model):
    for_rank = models.IntegerField()
    image_url = models.CharField(max_length=255)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'badge_master'


class Branch(models.Model):
    branchid = models.BigAutoField(db_column='Branchid', primary_key=True)  # Field name made lowercase.
    companyid = models.BigIntegerField(blank=True, null=True)
    branchname = models.CharField(max_length=250, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=205, blank=True, null=True)
    address3 = models.CharField(max_length=155, blank=True, null=True)
    city = models.CharField(max_length=105, blank=True, null=True)
    state = models.CharField(max_length=105, blank=True, null=True)
    country = models.CharField(max_length=55, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    mobile = models.CharField(max_length=45, blank=True, null=True)
    fax = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=105, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class Callevents(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    calldatetime = models.DateTimeField(db_column='CallDateTime', blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='Event', max_length=50, blank=True, null=True)  # Field name made lowercase.
    matuserid = models.CharField(db_column='MatUserID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'callevents'


class ChallengeBadges(models.Model):
    challenge_id = models.IntegerField()
    badge_image = models.CharField(max_length=255)
    badge_for_rank = models.IntegerField()
    created_by = models.CharField(max_length=45)
    creation_date = models.DateTimeField()
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_badges'


class Challenges(models.Model):
    challenge_type = models.CharField(max_length=45)
    created_by = models.CharField(max_length=45)
    challenge_title = models.CharField(max_length=100)
    challenge_target = models.CharField(max_length=10)
    challenge_startdate = models.DateTimeField()
    challenge_enddate = models.DateTimeField()
    challenge_details = models.CharField(max_length=500, blank=True, null=True)
    challenge_image = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField()
    last_updated_on = models.DateTimeField()
    last_updated_by = models.CharField(max_length=45)
    is_active = models.IntegerField(blank=True, null=True)
    challenge_counter = models.CharField(max_length=45)
    group_id = models.CharField(max_length=45, blank=True, null=True)
    group_name = models.CharField(max_length=45, blank=True, null=True)
    corporate_id = models.CharField(max_length=45, blank=True, null=True)
    corporate_name = models.CharField(max_length=45, blank=True, null=True)
    is_result_published = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenges'


class Company(models.Model):
    companyid = models.BigAutoField(db_column='companyId', primary_key=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='CompanyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(max_length=205, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=155, blank=True, null=True)
    state = models.CharField(max_length=105, blank=True, null=True)
    country = models.CharField(max_length=105, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=105, blank=True, null=True)
    licenseno = models.CharField(max_length=105, blank=True, null=True)
    licensevalidity = models.DateTimeField(blank=True, null=True)
    externalrefcode = models.CharField(max_length=45, blank=True, null=True)
    monitoring = models.IntegerField(blank=True, null=True)
    scan = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    policy = models.CharField(db_column='Policy', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class Companytypemaster(models.Model):
    comptypecode = models.CharField(db_column='Comptypecode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comtypename = models.CharField(db_column='Comtypename', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companytypemaster'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Firmwarehistory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    versionnumber = models.CharField(db_column='VersionNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    filesize = models.CharField(db_column='FileSize', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isnotificationsent = models.CharField(db_column='IsNotificationSent', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uploadedby = models.BigIntegerField(db_column='UploadedBy', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firmwarehistory'


class Groprepotdata(models.Model):
    groupid = models.CharField(db_column='GroupID', max_length=105, blank=True, null=True)  # Field name made lowercase.
    membercount = models.IntegerField(db_column='MemberCount', blank=True, null=True)  # Field name made lowercase.
    grouptitle = models.CharField(db_column='GroupTitle', max_length=500, blank=True, null=True)  # Field name made lowercase.
    owneruid = models.CharField(db_column='OwnerUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groprepotdata'


class Leaderboard(models.Model):
    challenge_id = models.IntegerField()
    participant_uid = models.CharField(max_length=45)
    rank = models.IntegerField(blank=True, null=True)
    target_achieved = models.DecimalField(max_digits=10, decimal_places=2)
    total_calories = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_reaction_count = models.IntegerField(blank=True, null=True)
    joined_on = models.DateTimeField()
    left_on = models.DateTimeField(blank=True, null=True)
    badge_image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leaderboard'


class LeaderboardReactions(models.Model):
    challenge_id = models.IntegerField(blank=True, null=True)
    reaction_type = models.CharField(max_length=45)
    reacted_by = models.CharField(max_length=45)
    reaction_date = models.DateTimeField()
    uid = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'leaderboard_reactions'


class Notificationfcmresponse(models.Model):
    notificationid = models.IntegerField(blank=True, null=True)
    targetplatform = models.CharField(db_column='targetPlatform', max_length=45, blank=True, null=True)  # Field name made lowercase.
    multicastid = models.CharField(max_length=805, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    failure = models.IntegerField(blank=True, null=True)
    canonicalids = models.CharField(max_length=800, blank=True, null=True)
    messageid = models.CharField(max_length=800, blank=True, null=True)
    resultmessage = models.CharField(max_length=7050, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    os = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificationfcmresponse'


class Notificationmaster(models.Model):
    notificationid = models.AutoField(primary_key=True)
    notificationtype = models.CharField(max_length=45, blank=True, null=True)
    apptarget = models.IntegerField(db_column='appTarget', blank=True, null=True)  # Field name made lowercase.
    notificationtitle = models.CharField(db_column='notificationTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notificationmessage = models.CharField(db_column='notificationMessage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    targetplatform = models.CharField(db_column='targetPlatform', max_length=45, blank=True, null=True)  # Field name made lowercase.
    imagename = models.CharField(db_column='imageName', max_length=805, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(blank=True, null=True)
    os = models.CharField(max_length=45, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=20000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificationmaster'


class Numbers(models.Model):
    n = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'numbers'


class Scanhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    companyid = models.BigIntegerField(blank=True, null=True)
    scannedby = models.BigIntegerField(blank=True, null=True)
    customeruid = models.CharField(db_column='customerUID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    healthstatus = models.CharField(max_length=45, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scanhistory'


class Userdatafromfirebase(models.Model):
    id = models.BigAutoField(primary_key=True)
    long = models.CharField(max_length=105, blank=True, null=True)
    uid = models.CharField(max_length=300, blank=True, null=True)
    deviceos = models.CharField(db_column='deviceOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lateshvitalsynchdate = models.DateTimeField(db_column='lateshVitalSynchDate', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='deviceID', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='AppVersion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    matinterest = models.IntegerField(db_column='MatInterest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userdatafromfirebase'


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


class UserinfoLl(models.Model):
    id = models.IntegerField()
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

    class Meta:
        managed = False
        db_table = 'userinfo_ll'
