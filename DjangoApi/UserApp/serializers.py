from rest_framework import serializers
from UserApp.models import Userinfo


class userinfoserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('uid','datecreated','deviceos','devicetype','isactive')
       
class Totaluserserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('uid','datecreated')

class Inactiveuserserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('isactive','datecreated')


class Activeuserserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('isactive','datecreated')

       
class Newuserserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('uid','datecreated')
       