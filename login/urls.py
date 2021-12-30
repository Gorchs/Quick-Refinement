from django.urls import path
from . import views

urlpatterns =[
    path('login/', views.login,name='Login'),
    path('organize/', views.login_organize,name='Organize Refinement'),
    path('participate/', views.login_participate,name='Participate Refinement'),

]
