from django.shortcuts import render

from django.http import HttpResponse

'''
The view that manages the Urls 
'''

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
