from django import forms
from django.conf import settings
import requests
from geo.models import Cities
import urllib
import json


class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['name']

    name = forms.CharField(max_length=100)

    def search(self, null=None):
        search_result = {}
        name = self.cleaned_data['name']
        url = ('https://restcountries.eu/rest/v2/capital/%s' % name)
        response = requests.get(url)
        if response.status_code == 200:
            search_result = requests.get(url).json()
        else:
            search_result['success'] = True
            search_result['message'] = 'No entry found for "%s"' % name
        return search_result
