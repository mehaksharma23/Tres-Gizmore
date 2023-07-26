from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from UserApp.models import Userinfo
from UserApp.serializers import userinfoserializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter




@csrf_exempt
def UserinfoApi(request,id=0):
    if request.method=='GET':
        user_info=Userinfo.objects.all()
        Userinfo_serializer=userinfoserializer(user_info,many=True)
        return JsonResponse(Userinfo_serializer.data,safe=False)
    elif request.method=='POST':
        Userinfo_data=JSONParser().parse(request)
        Userinfo_serializer=userinfoserializer(data=Userinfo_data)
        if Userinfo_serializer.is_valid():
            Userinfo_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to  Add",safe=False)
    elif request.method=='PUT':
        Userinfo_data=JSONParser().parse(request)
        user_info=Userinfo.objects.get(userid=Userinfo_data['uid'])
        Userinfo_serializer=userinfoserializer(user_info,data=Userinfo_data)
        if Userinfo_serializer.is_valid():
            Userinfo_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user_info=Userinfo.objects.get(userid=id)
        Userinfo.delete()
        return JsonResponse("Deleted Succesfully",safe=False)
    

class userinfoView(generics.ListAPIView):
    serializer_class=userinfoserializer
    queryset=Userinfo.objects.all()
    filter_backends=(DjangoFilterBackend, SearchFilter)
    filter_fields=('uid','datecreated','deviceos','devicetype','isactive')
    search_fields=('uid','datecreated','deviceos','devicetype','isactive')


  
    