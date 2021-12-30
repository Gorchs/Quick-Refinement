from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.core import serializers
# Create your views here.


def login_organize(request):
    return render(request,"organize.html")

def login_participate(request):
    return render(request,"participate.html")

def login(request):
    return render(request,"login.html")
