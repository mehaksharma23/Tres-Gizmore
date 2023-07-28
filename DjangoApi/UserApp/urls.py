from django.urls import include,re_path
from UserApp import views


urlpatterns = [
    re_path(r'^userinfo$',views.UserinfoApi),
    re_path(r'^summary$',views.SummaryAPI),
    re_path(r'^userinfo/([0-9]+)$',views.UserinfoApi)
]
