from django.urls import path
from . import views

app_name = "users"

urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    
]