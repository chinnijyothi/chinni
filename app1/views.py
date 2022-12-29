from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Reddy(request):
    return HttpResponse('my first view')