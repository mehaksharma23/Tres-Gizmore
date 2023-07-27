from django.urls import include,re_path
from UserApp import views


urlpatterns = [
    re_path('all_users/', views.all_users, name='all_users'),
    re_path(r'^userinfo$',views.UserinfoApi),
    re_path(r'^userinfo/([0-9]+)$',views.UserinfoApi)
]
