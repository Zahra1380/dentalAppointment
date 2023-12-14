from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('log-out/', views.LogOut.as_view(), name='log-out'),
    path('register', views.CheckToken.as_view(), name='register'),
    path('set-info', views.SetInfoView.as_view(), name='set-info'),
    path('sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.ChangePassword.as_view(), name='change-password'),
    path('forget-password/', views.ForgetPassword.as_view(), name='forget-password'),
]