from django.shortcuts import render
from django.http import HttpResponse

def first_APP1(request):

    return HttpResponse('<h1>this is first_APP1</h1>')
def second_APP1(request):
    
    return HttpResponse('<h1>this is second_APP1</h1>')
