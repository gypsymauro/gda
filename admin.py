from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Protocollo,ProtocolloAdmin)
admin.site.register(Fascicolo, FascicoloAdmin)
admin.site.register(Ufficio,UfficioAdmin)
admin.site.register(Ufficioprotocollo)
admin.site.register(Titolo)
admin.site.register(Alboprofessionale)
admin.site.register(Soggetto,SoggettoAdmin)
admin.site.register(Titolosoggetto)
admin.site.register(Utente,UtenteAdmin)
admin.site.register(Pratica,PraticaAdmin)
admin.site.register(Attribuzione, AttribuzioneAdmin)
admin.site.register(Fase, FaseAdmin)
admin.site.register(Praticaprotocollo)

