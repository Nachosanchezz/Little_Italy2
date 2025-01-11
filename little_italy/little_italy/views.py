from django.shortcuts import render
import requests

def home(request):
    api_url = "https://api.pizzas.com/v1/pizzas"
    response = requests.get(api_url)

    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = {"error": "No se pudo conectar con la API."}

    return render(request, "little_italy/home.html", {"api_data": api_data})

    