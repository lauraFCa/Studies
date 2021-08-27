from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Transacao
from .form import TransacaoForm
# Create your views here.

def home(request):
    data = {}
    data['Transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.now()
    # html = "<html><body>It is now %s</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['Transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm

    return render(request, 'contas/form.html', {'form': form})