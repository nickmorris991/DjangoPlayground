#from django.shortcuts import render
from django.http import HttpResponse

# view function for the /polls endpoint
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


