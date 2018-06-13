from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="gda/dashboard.html")),
    path('protocollo_list', views.ProtocolloList.as_view(), name='protocollo_list'),
    path('protocollo_view/<int:pk>', views.ProtocolloView.as_view(), name='protocollo_view'),
    path('protocollo_edit/<int:pk>', views.ProtocolloUpdate.as_view(), name='protocollo_edit'),

    path('pratica_list', views.PraticaList.as_view(), name='pratica_list'),
    path('pratica_view/<int:pk>', views.PraticaView.as_view(), name='pratica_view'),

    path('soggetto_list', views.SoggettoList.as_view(), name='soggetto_list'),
    path('soggetto_view/<int:pk>', views.SoggettoView.as_view(), name='soggetto_view'),

    
    
#    path('view/<int:pk>', views.ProtocolloView.as_view(), name='protocollo_view'),
#    path('edit/<int:pk>', views.ProtocolloUpdate.as_view(), name='protocollo_edit'),
#    path('delete/<int:pk>', views.ProtocolloDelete.as_view(), name='protocollo_delete'),
#    path('delete/<int:pk>', views.ProtocolloDelete.as_view(), name='protocollo_delete'),    
    url(r'^download/(\d+)/(\d+)$', views.download),
    path('accounts/', include('django.contrib.auth.urls')),

]
