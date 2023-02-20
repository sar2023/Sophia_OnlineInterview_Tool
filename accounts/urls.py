from django.urls import path
from accounts.views import * 


urlpatterns = [
    path('register/',registerPage,name='register'),
    path('afterlogin/',afterlogin,name='afterlogin'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
]
