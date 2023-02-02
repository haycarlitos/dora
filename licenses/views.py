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


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

