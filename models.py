# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .settings import *
from .cmis import *


from django.contrib import admin

# Register your models here.



class Ufficio(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    descrizione = models.CharField(max_length=254, blank=True, null=True)
    denominazione = models.CharField(max_length=500, blank=True, null=True)
    sportello = models.BooleanField()
    mittenteodestinatario = models.BooleanField()
    attribuzione = models.BooleanField()
    assessorato = models.BooleanField()
    pec = models.CharField(max_length=255, blank=True, null=True)
    richieste = models.BooleanField(null=True)

    class Meta:
        app_label = 'gda'
        managed = False
        db_table = 'ufficio'
        ordering = ['denominazione']

    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'

class UfficioAdmin(admin.ModelAdmin):
        model = Ufficio
        list_display = ['id','descrizione','denominazione','sportello']
        search_fields = ['id','descrizione']

    
class Ufficioprotocollo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    protocollo = models.ForeignKey('Protocollo', models.DO_NOTHING, db_column='protocollo', to_field='iddocumento', blank=True, null=True)
    ufficio = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='ufficio', to_field='id', blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'ufficioprotocollo'
        unique_together = (('protocollo', 'ufficio'),)
        ordering = ['ufficio']
        


class Ufficioutente(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    ospite = models.BooleanField()
    riservato = models.BooleanField()
    ricerca = models.BooleanField()
    visualizza = models.BooleanField()
    daiperletto = models.BooleanField()
    inseriscepratica = models.BooleanField()
    modificapratica = models.BooleanField()
    consolida = models.BooleanField()
    responsabile = models.BooleanField()
    procedimenti = models.BooleanField()
    leggepec = models.BooleanField()
    ufficio = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='ufficio', blank=True, null=True)
    utente = models.ForeignKey('Utente', models.DO_NOTHING, db_column='utente', blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'ufficioutente'

        
class Soggetto(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    codicefiscale = models.CharField(max_length=16, blank=True, null=True)
    cognome = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    nick = models.CharField(max_length=50, blank=True, null=True)
    denominazione = models.CharField(max_length=255, blank=True, null=True)
    denominazione2 = models.CharField(max_length=255, blank=True, null=True)
    denominazione3 = models.CharField(max_length=255, blank=True, null=True)
    ragionesociale = models.CharField(max_length=100, blank=True, null=True)
    partitaiva = models.CharField(max_length=11, blank=True, null=True)
    sessosoggetto = models.CharField(max_length=2, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    titolosoggetto = models.ForeignKey('Titolosoggetto', models.DO_NOTHING, db_column='titolosoggetto', blank=True, null=True)
    referente = models.CharField(max_length=100, blank=True, null=True)
    comunedinascita = models.CharField(max_length=100, blank=True, null=True)
    datanascita = models.DateField(blank=True, null=True)
    datacessazione = models.DateField(blank=True, null=True)
    descrizionecessazione = models.CharField(max_length=255, blank=True, null=True)
    alboprofessionale = models.ForeignKey('Alboprofessionale', models.DO_NOTHING, db_column='alboprofessionale', blank=True, null=True)
    provinciaalbo = models.CharField(max_length=2, blank=True, null=True)
    numeroiscrizionealbo = models.CharField(max_length=15, blank=True, null=True)
    indicepao = models.CharField(max_length=255, blank=True, null=True)
    indicepaaoo = models.CharField(max_length=255, blank=True, null=True)
    residente = models.BooleanField(null=True)
    codiceanagrafe = models.CharField(max_length=255, blank=True, null=True)
    tipocittadino = models.CharField(max_length=255, blank=True, null=True)
    condizionecittadino = models.CharField(max_length=255, blank=True, null=True)
    codicepitre = models.CharField(max_length=255, blank=True, null=True)
    ragionesociale1 = models.CharField(max_length=255, blank=True, null=True)

    def comesichiama(self):
        den = ''
        if self.cognome:
            den = self.cognome +' '+ self.nome
        if self.ragionesociale:
            den = self.ragionesociale
        if self.denominazione:
            den = self.denominazione

        return den

            
    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'soggetto'
        ordering = ['cognome','nome','ragionesociale','denominazione']

    def __str__(self):

        return self.comesichiama() + '[' + str(self.id) + ']'

  
        

class SoggettoAdmin(admin.ModelAdmin):
        model = Soggetto
        list_display = ['id','cognome','nome','codicefiscale','denominazione','ragionesociale']
        search_fields = ['id','cognome','nome','codicefiscale','denominazione','ragionesociale', ]
        ordering = ['cognome','nome','codicefiscale','denominazione','ragionesociale']




class Soggettoprotocollo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    titolo = models.ForeignKey('Titolo', models.DO_NOTHING, db_column='titolo', blank=True, null=True)
    protocollo = models.ForeignKey('Protocollo', models.DO_NOTHING, db_column='protocollo', to_field='iddocumento', blank=True, null=True)
    soggetto = models.ForeignKey('Soggetto', models.DO_NOTHING, db_column='soggetto', blank=True, null=True)
    corrispondenza = models.BooleanField()
    notifica = models.BooleanField()
    conoscenza = models.BooleanField()
    primoinserimento = models.BooleanField()
    datainizio = models.DateField(blank=True, null=True)
    datafine = models.DateField(blank=True, null=True)
    annullato = models.BooleanField()
    principale = models.BooleanField()
    soggettoreferente = models.ForeignKey('Soggetto', models.DO_NOTHING, db_column='soggettoreferente', related_name='soggettoreferente', blank=True, null=True)
    abilitatoweb = models.BooleanField()
    note = models.CharField(max_length=255, blank=True, null=True)
    pec = models.BooleanField()
    messaggiopec = models.BigIntegerField(blank=True, null=True)
    indirizzo = models.CharField(max_length=1024, blank=True, null=True)


    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'soggettoprotocollo'
    


PROTOCOLLOTIPO_CHOICES = (
    ('ESTERNO', 'ESTERNO'),
    ('INTERNO', 'INTERNO'),
    ('USCITA', 'USCITA'),
)

class Protocollo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=PROTOCOLLOTIPO_CHOICES, blank=False, null=False)
    anno = models.IntegerField()
    iddocumento = models.CharField(unique=True, max_length=12)
    dataprotocollo = models.DateTimeField()
    sportello = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='sportello')
    oggetto = models.CharField(max_length=1024)
    note = models.CharField(max_length=1024, blank=True, null=True)
    tiporiferimentomittente = models.CharField(max_length=25, blank=True, null=True)
    riferimentomittente = models.CharField(max_length=255, blank=True, null=True)
    datariferimentomittente = models.DateField(blank=True, null=True)
    riservato = models.BooleanField()
    convalidaattribuzioni = models.BooleanField()
    dataconvalidaattribuzioni = models.DateTimeField(blank=True, null=True)
    esecutoreconvalidaattribuzioni = models.CharField(max_length=40, blank=True, null=True)
    convalidaprotocollo = models.BooleanField()
    numeroconvalidaprotocollo = models.CharField(max_length=10, blank=True, null=True)
    dataconvalidaprotocollo = models.DateTimeField(blank=True, null=True)
    esecutoreconvalidaprotocollo = models.CharField(max_length=40, blank=True, null=True)
    consolidadocumenti = models.BooleanField()
    dataconsolidadocumenti = models.DateTimeField(blank=True, null=True)
    esecutoreconsolidadocumenti = models.CharField(max_length=40, blank=True, null=True)
    numeroricevuta = models.CharField(max_length=10, blank=True, null=True)
    dataricevuta = models.DateTimeField(blank=True, null=True)
    annullamentorichiesto = models.BooleanField()
    annullato = models.BooleanField()
    corrispostoostornato = models.BooleanField()
    richiederisposta = models.BooleanField()
    spedito = models.BooleanField()
    dataspedizione = models.DateTimeField(blank=True, null=True)
    esecutorespedizione = models.CharField(max_length=40, blank=True, null=True)
    controlloreposta = models.CharField(max_length=40, blank=True, null=True)
    scansionemassiva = models.BooleanField(null=True)
    fascicolo = models.ForeignKey('Fascicolo', models.DO_NOTHING, db_column='fascicolo', blank=True, null=True)
    numeroatto = models.IntegerField(blank=True, null=True)
    dataatto = models.DateField(blank=True, null=True)
    cartelladocer = models.CharField(max_length=1024,blank=True, null=True)
    tipoarchivio = models.CharField(max_length=1024,blank=True, null=True)

    uffici = models.ManyToManyField(Ufficio, through='Ufficioprotocollo', related_name='uffici')
    soggetti = models.ManyToManyField(Soggetto, through='Soggettoprotocollo', through_fields=('protocollo','soggetto'), related_name='soggetti' )        
    attribuzione_uffici = models.ManyToManyField(Ufficio, through='Attribuzione', related_name='attribuzione_uffici')
 
    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'protocollo'


    def DocumentList(self):
        
        cmis = Cmis(GDACONFIG)
        if not cmis.login():
            print('out')
            exit(1)


        path = cmis.getDocPath(self.iddocumento,self.dataprotocollo)
        files=cmis.getChilds(path)
        return files


class ProtocolloAdmin(admin.ModelAdmin):
        model = Protocollo
        list_display = ['iddocumento','oggetto','tipo','dataprotocollo']
        search_fields = ['iddocumento','oggetto']
        autocomplete_fields = ['fascicolo','uffici']


        


class Pratica(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    anno = models.IntegerField()
    datapratica = models.DateField(blank=True, null=True)
    idpratica = models.CharField(unique=True, max_length=9)
    tipo = models.ForeignKey('Tipopratica', models.DO_NOTHING, db_column='tipo')
    codiceinterno = models.CharField(unique=True, max_length=50)
    codiceaggiuntivo = models.CharField(max_length=50, blank=True, null=True)
    descrizione = models.CharField(max_length=1024)
    note = models.CharField(max_length=6144, blank=True, null=True)
    attribuzione = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='attribuzione')
    gestione = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='gestione',related_name='ufficio_gestione')
    ubicazione = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='ubicazione', blank=True, null=True,related_name='ufficio_ubicazione')
    dettaglioubicazione = models.CharField(max_length=255, blank=True, null=True)
    fase = models.ForeignKey('Fase', models.DO_NOTHING, db_column='fase', blank=True, null=True)
    fascicolo = models.ForeignKey('Fascicolo', models.DO_NOTHING, db_column='fascicolo')
    riservata = models.BooleanField()
    archiviata = models.BooleanField()
    annoinventario = models.IntegerField(blank=True, null=True)
    numeroinventario = models.CharField(max_length=10, blank=True, null=True)
    datachiusura = models.DateField(blank=True, null=True)
    datatermineistruttoria = models.DateField(blank=True, null=True)
    datascadenza = models.DateField(blank=True, null=True)
    procedimento = models.BigIntegerField(blank=True, null=True)
    codificaanomala = models.BooleanField()
    multiufficio = models.BooleanField()

    praticheprotocolli = models.ManyToManyField(Protocollo, through='Praticaprotocollo', related_name='praticheprotocolli')    

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'pratica'


        
class PraticaAdmin(admin.ModelAdmin):
    model = Pratica
    list_display = ['id','idpratica','codiceinterno','anno','datapratica','descrizione','gestione']
    
    search_fields = ['codiceinterno','descrizione']
    ordering = ['-idpratica']
 #        exclude = ['soggetto']




class Fascicolo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    categoria = models.IntegerField()
    classe = models.IntegerField()
    descrizione = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=2048, blank=True, null=True)
    fascicolo = models.IntegerField()
    dal = models.DateField(blank=True, null=True)
    al = models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'fascicolo'

    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'

        
class FascicoloAdmin(admin.ModelAdmin):
        model = Fascicolo
        list_display = ['id','categoria','classe','descrizione']
        search_fields = ['descrizione']
        


    

class Titolo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    descrizione = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'titolo'

    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'
        

class Alboprofessionale(models.Model):
    id = models.BigAutoField(primary_key=True)
    descrizione = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'alboprofessionale'

    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'

        
class Titolosoggetto(models.Model):
    descrizione = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'titolosoggetto'


    def __str__(self):
        return self.descrizione
        


class Utente(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    amministratore = models.BooleanField(null=True)
    attributoreprotocollo = models.BooleanField()
    email = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=40, blank=True, null=True)
    modellatorepratiche = models.BooleanField()
    nome = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)
    operatoreanagrafiche = models.BooleanField()
    operatorepratiche = models.BooleanField()
    operatoreprotocollo = models.BooleanField()
    password = models.CharField(max_length=255, blank=True, null=True)
    superutente = models.BooleanField()
    supervisoreanagrafiche = models.BooleanField()
    supervisorepratiche = models.BooleanField()
    supervisoreprotocollo = models.BooleanField()
    ricercatoreprotocollo = models.BooleanField()
    istruttorepratiche = models.BooleanField()
    pubblicaalbo = models.BooleanField()
    disabilitato = models.BooleanField()
    soggetto = models.ForeignKey('Soggetto', models.DO_NOTHING, db_column='soggetto', blank=True, null=True)
    spedisceprotocollo = models.BooleanField()
    attributorepratiche = models.BooleanField()
    nuovodocsuconsolidato = models.BooleanField()
    operatoreurp = models.BooleanField()
    supervisoreurp = models.BooleanField()
    richieste = models.BooleanField(null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'utente'


class UtenteAdmin(admin.ModelAdmin):
        model = Utente
        list_display = ['id','login','nome','sigla','amministratore']
        search_fields = ['login','nome','sigla']
        ordering = ['login']
        autocomplete_fields = ['soggetto']


class Tipopratica(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    codice = models.CharField(unique=True, max_length=10, blank=True, null=True)
    descrizione = models.CharField(max_length=255, blank=True, null=True)
    tipopadre = models.ForeignKey('self', models.DO_NOTHING, db_column='tipopadre', blank=True, null=True)
    formulacodifica = models.CharField(max_length=255, blank=True, null=True)
    lunghezzaprogressivo = models.IntegerField(blank=True, null=True)
    progressivoanno = models.BooleanField()
    progressivogiunta = models.BooleanField()
    fascicolo = models.ForeignKey('Fascicolo', models.DO_NOTHING, db_column='fascicolo', blank=True, null=True)
    foglia = models.BooleanField()
    approvata = models.BooleanField()
    obsoleta = models.BooleanField()

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'tipopratica'
        
    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'

        

 


class Oggetto(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    descrizione = models.CharField(max_length=255, blank=True, null=True)
    associasoggettopratica = models.BooleanField()

    class Meta:
        app_label = 'gda'
        managed = False
        db_table = 'oggetto'


class Praticaprotocollo(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    oggetto = models.ForeignKey('Oggetto', models.DO_NOTHING, db_column='oggetto', blank=True, null=True)
    pratica = models.ForeignKey('Pratica', models.DO_NOTHING, db_column='pratica', to_field='idpratica')
    protocollo = models.ForeignKey('Protocollo', models.DO_NOTHING, db_column='protocollo', to_field='iddocumento')
    originale = models.BooleanField()


    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'praticaprotocollo'

   
class Attribuzione(models.Model):
    rec_creato = models.DateTimeField()
    rec_creato_da = models.CharField(max_length=40, blank=True, null=True)
    rec_modificato = models.DateTimeField(blank=True, null=True)
    rec_modificato_da = models.CharField(max_length=40, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    protocollo = models.ForeignKey('Protocollo', models.DO_NOTHING, db_column='protocollo', to_field='iddocumento')
    ufficio = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='ufficio', related_name='attruff')
    dataattribuzioneprotocollo = models.DateTimeField(blank=True, null=True)
    letto = models.BooleanField()
    dataletto = models.DateTimeField(blank=True, null=True)
    esecutoreletto = models.CharField(max_length=40, blank=True, null=True)
    principale = models.BooleanField()
    evidenza = models.CharField(max_length=1, blank=True, null=True)
    dataprincipale = models.DateTimeField(blank=True, null=True)
    esecutoreprincipale = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'attribuzione'
        unique_together = (('ufficio', 'protocollo'),)

class AttribuzioneAdmin(admin.ModelAdmin):
        model = Attribuzione
        list_display = ['id','protocollo','ufficio']
        autocomplete_fields = ['protocollo','ufficio']
     
        


class Fase(models.Model):
    id = models.BigAutoField(primary_key=True)
    descrizione = models.CharField(max_length=255)
    esclusivadaufficio = models.ForeignKey('Ufficio', models.DO_NOTHING, db_column='esclusivadaufficio', blank=True, null=True)
    istruttoria = models.BooleanField(null=True)
    evidenza = models.BooleanField()

    class Meta:
        app_label = 'gda'        
        managed = False
        db_table = 'fase'

    def __str__(self):
        return self.descrizione + '[' + str(self.id) + ']'
        

class FaseAdmin(admin.ModelAdmin):
        model = Fase
        list_display = ['id','descrizione']
        search_fields = ['descrizione']

