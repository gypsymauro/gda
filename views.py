
# Create your views here.


from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gda.models import *

from .cmis import *
from .settings import *




class ProtocolloList(ListView):
    model = Protocollo
    paginate_by = 10
    ordering = ['-dataprotocollo']

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        page = self.request.GET.get('page', None)
        username = self.request.user.username
        if not search and not page:
            return self.model.objects.none()

        if 'soggetto:' in search:
            search=search.replace('soggetto:','')
            print(search)
            object_list = self.model.objects.filter(soggetti__in = [search],  attribuzione_uffici__ufficioutente__utente__login=username)
        else:
            object_list = self.model.objects.filter(oggetto__icontains = search, attribuzione_uffici__ufficioutente__utente__login=username).order_by('-dataprotocollo')
        return object_list

class ProtocolloView(DetailView):
    model = Protocollo


class ProtocolloDetail(DetailView):
    model = Protocollo


def download(request, iddocumento, numdoc):
    if not request.user.is_authenticated:
        html = "No way"
        response = HttpResponse(html)
        return response
    
    fl = Protocollo.objects.get(iddocumento=iddocumento).DocumentList()

    response = HttpResponse()

    print(fl)
    for f in fl:
        if int(f['id'])==int(numdoc):
            cmis = Cmis(GDACONFIG)
            if not cmis.login():
                print('out')
                exit(1)

            print(f['cmispath'])
            print(cmis.getFile(f['cmispath']))                
            contents = cmis.getFile(f['cmispath'])

            response = HttpResponse(contents)
            response['Content-Disposition'] = 'attachment; filename="%s"' % (f['path'])
    return response 
 

class ProtocolloCreate(CreateView):
    model = Protocollo
    fields = ['oggetto']
    success_url = reverse_lazy('protocollo_list')

class ProtocolloUpdate(UpdateView):
    model = Protocollo
    fields = ['oggetto']
    success_url = reverse_lazy('protocollo_list')

class ProtocolloDelete(DeleteView):
    model = Protocollo
    success_url = reverse_lazy('protocollo_list')




class PraticaList(ListView):
    model = Pratica
    paginate_by = 10
    ordering = ['-datapratica']
    
    def get_queryset(self):
        search = self.request.GET.get('search', None)
        page = self.request.GET.get('page', None)                
        if not search and not page:
            return self.model.objects.none()
        if 'soggetto:' in search:
            search=search.replace('soggetto:','')
            print(search)
            object_list = self.model.objects.filter(soggetti__in = [search])
        else:       
            object_list = self.model.objects.filter(descrizione__icontains = search).order_by('-datapratica')
        return object_list

class PraticaView(DetailView):
    model = Pratica

class PraticaDetail(DetailView):
    model = Pratica

    
class SoggettoList(ListView):
    model = Soggetto
    paginate_by = 10
    
    def get_queryset(self):
        search = self.request.GET.get('search', None)
        page = self.request.GET.get('page', None)                
        if not search and not page:
            return self.model.objects.none()
        object_list = self.model.objects.filter(cognome__icontains = search) | self.model.objects.filter(denominazione__icontains = search) | self.model.objects.filter(ragionesociale__icontains = search) | self.model.objects.filter(codicefiscale__icontains = search) | self.model.objects.filter(partitaiva__icontains = search)
        return object_list

class SoggettoView(DetailView):
    model = Soggetto

class SoggettoDetail(DetailView):
    model = Soggetto

    
