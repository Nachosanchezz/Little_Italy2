from django.shortcuts import render
import requests

def home(request):
    return render(request, "little_italy/home.html")
   
    