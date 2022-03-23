from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def add(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    data = {'result': arg1 + arg2}
    _json = json.dumps(data)
    return HttpResponse(_json)


def subtract(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    return HttpResponse(arg1 - arg2)


def multiply(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    return HttpResponse(arg1 * arg2)


def divide(request, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    return HttpResponse(arg1 / arg2)