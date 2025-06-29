from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Servico, Sistema

def BASE(request):
    return render(request, 'base.html')


def index(request):
    slides = [
        {'img': 'assets/dist/img/maraba_1.jpg', 'alt': 'Banner 1', 'title': 'TRABALHANDO O DESENVOLVIMENTO URBANO', 'subtitle': 'E A REGULARIZAÇÃO FUNDIÁRIA DE MARABÁ'},
        {'img': 'assets/dist/img/maraba2.jpg',  'alt': 'Banner 2', 'title': 'MAIS DE 120 FAMÍLIAS BENEFICIADAS', 'subtitle': 'Nova etapa de regularização fundiária em andamento'},
        {'img': 'assets/dist/img/Maraba-OK_E.webp', 'alt': 'Banner 3', 'title': 'MAPA URBANO INTERATIVO', 'subtitle': 'Acesse informações da cidade em tempo real'},
        {'img': 'assets/dist/img/idurb_Maraba_2.jpeg', 'alt': 'Banner 4', 'title': 'Instituto de Desenvolvimento Urbano de Marabá - IDURB', 'subtitle': 'Instituto de Desenvolvimento Urbano de Marabá'},
        {'img': 'assets/dist/img/idurb_Maraba_3.jpeg', 'alt': 'Banner 5', 'title': 'Ações e entregas do IDURB', 'subtitle': 'O IDURB está inovando, trazendo novas tecnologias para melhor atender a população'},
    ]
    return render(request, 'site/index.html', {'slides': slides})


def sobre(request):
    return render(request, 'webapp/sobre.html')


# webapp/views.py
from django.shortcuts import render, redirect
from .models import MensagemContato  # Importar o novo model
from django.contrib import messages

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        if nome and email and mensagem:
            MensagemContato.objects.create(nome=nome, email=email, mensagem=mensagem)
            messages.success(request, "Sua mensagem foi enviada com sucesso!")
            return redirect('contato')
        else:
            messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
    
    return render(request, 'site/contato.html')



def detalhe_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'webapp/detalhe_noticia.html', {'noticia': noticia})


def o_idurb(request):
    return render(request, 'site/oidurb.html')


def legislacao(request):
    return render(request, 'site/legislacao.html')


def servicos(request):
    return render(request, 'site/servicos.html')


def transparencia(request):
    return render(request, 'site/transparencia.html')


def mapa(request):
    return render(request, 'site/mapa.html')
