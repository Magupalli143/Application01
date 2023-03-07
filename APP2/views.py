from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second_APP2(request):
    return HttpResponse('this is second_APP2')

def two_APP2(request):
    return HttpResponse('this is two_APP2')