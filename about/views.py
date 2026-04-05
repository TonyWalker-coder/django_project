from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def about_me(request):
    return HttpResponse("Tony's About Page!")