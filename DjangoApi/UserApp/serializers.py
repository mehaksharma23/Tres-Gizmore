from rest_framework import serializers
from UserApp.models import Userinfo


class userinfoserializer(serializers.ModelSerializer):
    class Meta:
       model=Userinfo
       fields=('uid','datecreated','deviceos','devicetype','isactive')
       

       