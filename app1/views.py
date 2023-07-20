from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(request):
    return HttpResponse('<h1>How Are You!!!</h1>')
def wish(request):
    return HttpResponse('<h1>i am Fine</h1>')