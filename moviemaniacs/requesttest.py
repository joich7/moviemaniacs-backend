import requests
from django.http import JsonResponse
from django.shortcuts import render
from requests.auth import HTTPBasicAuth


r = requests.get('https://api.github.com / user, ',
                 auth=HTTPBasicAuth('user', 'pass'))
data = [{'name': 'Peter', 'email': 'peter@example.org'},
        {'name': 'Julia', 'email': 'julia@example.org'}]
data = r.json()
return JsonResponse(data, safe=False)
