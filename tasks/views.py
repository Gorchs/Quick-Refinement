from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
# Create your views here.

import random
from tasks.models  import Task

def get_tasks(request):
    all_entries = serializers.serialize("json", Task.objects.all())
    if all_entries == None:
        return None
    return JsonResponse(all_entries,safe=False)

def get_task(request,task_id):
        task_object=Task.objects.get(id=task_id)
        if task_object==None:
            data=""
        else:
            data={
            "id":task_id,
            "link":task_object.link,
            "header":task_object.header,
            "description":task_object.description
            }
        return JsonResponse(data)
