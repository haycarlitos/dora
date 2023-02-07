from django.http import HttpResponse
from .models import Client, License
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render

''' 
def index(request):
    client = Client.objects.get(pk=1)
    licenses = client.licenses.all()
   # template = loader.get_template('licenses/index.html')
    context = {
        'client': client,
        'licenses': licenses,
    }
    return render(request, 'licenses/index.html', context)

def client(request, client_id):
    return HttpResponse("You're looking at client %s." % client_id)
'''
def index(request):
    client_list = Client.objects.all()
    context = {
        'client_list': client_list
    }
    return render(request, 'licenses/index.html', context)

def client(request, client_id):
    client = Client.objects.get(pk=client_id)
    licenses = client.licenses.all()
    active_licenses = []
    for l in licenses:
        if(l.is_expired()==False):
            active_licenses.append(l)
    
    context = {
        'client': client,
        'licenses': active_licenses,
    }
    return render(request, 'licenses/active_licenses.html', context)

def license(request, license_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % license_id)

def detail(request, license_id):
    license = get_object_or_404(License, pk=license_id)
    return render(request, 'licenses/detail.html', {'license': license})

