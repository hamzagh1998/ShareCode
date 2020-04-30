from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('complete_profile/', views.completeProfile, name='complete_profile'),
    path('user_profile/<int:id>/', views.profileView, name='user_profile'),
]
