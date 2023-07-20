from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
    return HttpResponse('<marquee><h1>2nd App View Response 1</h1></marquee>')
def main(request):
    return HttpResponse('<marquee><h1>2nd App View Response 2</h1></marquee>')