from django.shortcuts import render
from tasks.models import Task

def home_view(request):

    queryset = Task.objects.all()
    context={
        "task":queryset
        }

    return render(request, "login.html",context)
