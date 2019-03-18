from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello :D")


def number(request, num):
    resp = "<html><body><h1>{}</h1></body></html>".format(num)
    return HttpResponse(resp)
