from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('homeloan',views.predictor),
    path('result',views.formInfo),
    path('result_edu',views.formInfo_edu),
    path('result_vehi',views.formInfo_vehi),
    path('result_per',views.formInfo_per),
    path('dash',views.dashboard,name='dashboard'),
    path('loginn',views.user_loginmain,name='loginn'),
    path('loginmain', views.user_loginmain), 
    path('signup',views.signup),
    path('logout',views.logout),
    path('login_sub',views.login),
    path('eduloan',views.eduloan),
    path('perloan',views.perloan),
    path('vehiloan',views.vehiloan),
    
]