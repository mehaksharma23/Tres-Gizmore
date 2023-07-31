from django.urls import include,re_path
from UserApp import views


urlpatterns = [
    re_path(r'^userinfo$',views.UserinfoApi),
    re_path(r'^summary$',views.SummaryAPI),
    re_path(r'^inactive$',views.InactiveUserAPI),
    re_path(r'^active$',views.ActiveUserAPI),
    re_path(r'^new$',views.NewUserAPI),
    re_path(r'^new/([0-9]+)$',views.NewUserAPI),
    re_path(r'^userinfo/([0-9]+)$',views.UserinfoApi),
    re_path(r'^summary/([0-9]+)$',views.SummaryAPI),
    re_path(r'^inactive/([0-9]+)$',views.InactiveUserAPI),
    re_path(r'^active/([0-9]+)$',views.ActiveUserAPI),
]
