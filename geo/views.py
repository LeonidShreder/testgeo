from django.shortcuts import render
import requests
import urllib
import json
from .forms import CitiesForm

# def home(request):
#     city = {}
#     if 'name' in request.GET:
#         where = request.GET['city']
#         (
#         response = requests.get
#     return render(request, 'home.html', {'city': city})


def home(request):
    search_result = {}
    if 'name' in request.GET:
        form = CitiesForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = CitiesForm()
    return render(request, 'home.html', {'form': form, 'search_result': search_result})
