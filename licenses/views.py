'''
from django.views.generic import TemplateView
from .models import Client, License

class ClientDetailView(TemplateView):
    """A view to show the details of a particular client and their license information.
    """
    template_name = 'client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(pk=client_id)
        licenses = client.licenses.all()
        context['client'] = client
        context['licenses'] = licenses
        return context
'''        
from django.http import HttpResponse

from .models import Client, License

def index(request):
    licenses_list = License.objects.order_by('-expiration_date')[:5]
    output = ', '.join([q.package_name for q in licenses_list])
    return HttpResponse(output)

def client(request, client_id):
    return HttpResponse("You're looking at client %s." % client_id)

def license(request, license_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % license_id)


