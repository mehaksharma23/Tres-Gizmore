from django.urls import include,re_path
from UserApp import views


urlpatterns = [
    re_path(r'^userinfo$',views.UserinfoApi),
    re_path(r'^summary$',views.SummaryAPI),
    re_path(r'^lastactivedays$',views.lastactivedaysAPI),
    re_path(r'^userinfo/([0-9]+)$',views.UserinfoApi),
    re_path(r'^summary/([0-9]+)$',views.SummaryAPI),
    re_path(r'^lastactivedays/([0-9]+)$',views.lastactivedaysAPI)
]
