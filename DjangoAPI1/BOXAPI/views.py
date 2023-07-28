from django.shortcuts import render
from django.db import connection

cursor = connection.cursor()
def allusers(req):
        cursor.execute('call Get_number_of_users')
        result = cursor.fetchall()
        return render(req, 'all_users.html', {'result': result})      

  
