from django.urls import path
from . import views

urlpatterns = [#ip주소/
    path('', views.homepage),
    path('mypage/',views.mypage),     #Ip주소/
    path('companypage/', views.companypage), #IP주소/about_me/
]