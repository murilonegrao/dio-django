from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello, {nome} de {idade} anos</h1>')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
