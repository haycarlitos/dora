from django.http import HttpResponse
from .models import Client, License
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render

'''
class ClientDetailView(TemplateView):
    """A view to show the details of a particular client and their license information.
    """
    template_name = 'licenses/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(pk=client_id)
        licenses = client.licenses.all()
        context = {
            'client': client,
            'licenses': licenses,
        }
        return context
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
'''
def index(request):
    licenses_list = License.objects.order_by('-expiration_date')[:5]
    template = loader.get_template('licenses/index.html')
    context = {
        'licenses': licenses_list,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    licenses_list = License.objects.order_by('-expiration_date')[:5]
    output = ', '.join([q.package_name for q in licenses_list])
    return HttpResponse(output)
'''
def client(request, client_id):
    return HttpResponse("You're looking at client %s." % client_id)

def license(request, license_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % license_id)

def detail(request, license_id):
    license = get_object_or_404(License, pk=license_id)
    return render(request, 'licenses/detail.html', {'license': license})

