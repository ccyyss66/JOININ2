from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def schoolManage(request):
    session_userId = request.session.get('userId')
    return render(request, "system/schoolManage.html", {"session_userId":session_userId})

def index(request):
    session_userId = request.session.get('userId')
    return render(request,"system/index.html",{"session_userId":session_userId})

def addSchool(request):
    return render(request, "system/addSchool.html")

def organize(request):
    return render(request,"system/organize.html")

def test(request):
    return render(request,'system/test.html')