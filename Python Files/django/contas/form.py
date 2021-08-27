from django.db.models.base import Model
from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):
    # metadados que recebem os fiels
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
