from django.urls import path
from . import views

urlpatterns =[
    path('get_tasks/', views.get_tasks),
    path('get_task/<str:task_id>/', views.get_task)
]
