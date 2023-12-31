from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from DjangoApi.settings import DATABASES
from UserApp.models import Userinfo
from UserApp.serializers import userinfoserializer, Totaluserserializer,Inactiveuserserializer,Activeuserserializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db import connection
import datetime
import pandas as pd 

cursor=connection.cursor()


@csrf_exempt
def UserinfoApi(request,id=0):
    if request.method=='GET':
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date','')
        user_info = Userinfo.objects.filter(datecreated__range=[start_date,end_date])
        print(start_date)
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

@csrf_exempt
def SummaryAPI(request,id=0):
    if request.method=='GET':
       row_count=Userinfo.objects.count()
       data= {
           'row_count':row_count
       }
       return JsonResponse(data)
    
@csrf_exempt
def InactiveUserAPI(request,id=0):
    if request.method=='GET':
       inactive_user=Userinfo.objects.filter(isactive=False).count()
      
       data= {
           'inactive_user':inactive_user
       }
       return JsonResponse(data)
    
@csrf_exempt
def ActiveUserAPI(request,id=0):
    
    if request.method=='GET':
       active_user=Userinfo.objects.filter(isactive=True).count()
      
       data= {
           'active_user':active_user
       }
       return JsonResponse(data)    
    
@csrf_exempt
def NewUserAPI(request,id=0):
    from datetime import timedelta
    from django.utils import timezone
    


    if request.method=='GET':
       end_date=timezone.now()
       start_date=end_date-timedelta(days=7)

       new_user=Userinfo.objects.filter(datecreated__range=[start_date,end_date]).count()
      
       data= {
           'new_user':new_user
       }
       return JsonResponse(data)    
   


class userinfoView(generics.ListAPIView):
    serializer_class=userinfoserializer
    queryset=Userinfo.objects.all()
    filter_backends=(DjangoFilterBackend, SearchFilter)
    filter_fields=('uid','datecreated','deviceos','devicetype','isactive')
    search_fields=('uid','datecreated','deviceos','devicetype','isactive')


