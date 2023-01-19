from django.http import HttpResponse
from django.shortcuts import render

def my_view(request):
    return HttpResponse('MY FIRST VIEW')


def home(request):
    return HttpResponse('HOME') 


def contato(request):
    return HttpResponse('CONTATO')
