from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from DjangoApi.settings import DATABASES
from UserApp.models import Userinfo
from UserApp.serializers import userinfoserializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db import connection

cursor=connection.cursor()


@csrf_exempt
def UserinfoApi(request,id=0):
    if request.method=='GET':
        
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date','')
        user_info = Userinfo.objects.filter(datecreated__range=(start_date, end_date))
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
        cursor.execute("SELECT count(*) AS TotalRows FROM careatwork.userinfo")
        row = cursor.fetchone()
        return JsonResponse('Here are the total number of users', row, safe=False)
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


