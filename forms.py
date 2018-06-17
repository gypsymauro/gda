from django import forms

from .models import Protocollo

class ProtocolloForm(forms.ModelForm):
    oggetto = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Protocollo
        fields = ('tipo','oggetto','sportello','uffici','attribuzione_uffici')

