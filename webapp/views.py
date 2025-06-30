from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Servico, Sistema

def BASE(request):
    return render(request, 'base.html')


def index(request):
    slides = [
        {'img': 'assets/dist/img/maraba_1.jpg', 'alt': 'Banner 1', 'title': 'TRABALHANDO O DESENVOLVIMENTO URBANO', 'subtitle': 'E A REGULARIZAÇÃO FUNDIÁRIA DE MARABÁ'},
        {'img': 'assets/dist/img/maraba2.jpg',  'alt': 'Banner 2', 'title': 'MAIS DE 120 FAMÍLIAS BENEFICIADAS', 'subtitle': 'Nova etapa de regularização fundiária em andamento'},
        {'img': 'assets/dist/img/Maraba-OK_E.webp', 'alt': 'Banner 3', 'title': 'MAPA URBANO INTERATIVO', 'subtitle': 'Acesse informações da cidade em tempo real'},
        {'img': 'assets/dist/img/idurb_Maraba_2.jpeg', 'alt': 'Banner 4', 'title': 'Secretaria de Desenvolvimento Urbano de Marabá - SDU', 'subtitle': 'Secretaria de Desenvolvimento Urbano de Marabá'},
        {'img': 'assets/dist/img/idurb_Maraba_3.jpeg', 'alt': 'Banner 5', 'title': 'Ações e entregas da SDU', 'subtitle': 'A SDU está inovando, trazendo novas tecnologias para melhor atender a população'},
    ]
    return render(request, 'site/index.html', {'slides': slides})


def sobre(request):
    return render(request, 'webapp/sobre.html')


from django.contrib import messages
from django.shortcuts import render

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        # Exemplo: salvar ou enviar e-mail (aqui apenas uma mensagem de sucesso)
        messages.success(request, 'Mensagem enviada com sucesso! Em breve entraremos em contato.')

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



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/painel/')  # Redireciona ao painel após login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # ou a URL desejada



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def painel_admin(request):
    return render(request, 'painel/index.html')



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def painel_view(request):
    return render(request, 'painel.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')  # ou o nome real do seu template


from django.shortcuts import render

def noticias_listar(request):
    return render(request, 'noticias/listar.html')  # ajuste o caminho do template

from django.shortcuts import render

def servicos_listar(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/listar.html', {'servicos': servicos})



from django.shortcuts import render
from .models import Sistema  # ajuste o nome do seu model

def sistemas_listar(request):
    sistemas = Sistema.objects.all()
    return render(request, 'sistemas/listar.html', {'sistemas': sistemas})


from django.shortcuts import render

def equipe_listar(request):
    return render(request, 'institucional/equipe_listar.html')  # ajuste o caminho conforme seus templates


from django.shortcuts import render

def organograma(request):
    return render(request, 'institucional/organograma.html')  # ajuste se o path for diferente


from django.shortcuts import render

def relatorios_view(request):
    return render(request, 'transparencia/relatorios.html')  # ajuste o path do template conforme seu projeto


from django.shortcuts import render

def prestacao_contas_view(request):
    return render(request, 'transparencia/prestacao_contas.html')


from django.shortcuts import render

def planejamento_view(request):
    return render(request, 'institucional/planejamento.html')


from django.shortcuts import render

def plano_diretor_view(request):
    return render(request, 'institucional/plano_diretor.html')


from django.shortcuts import render

def codigo_obras_view(request):
    return render(request, 'legislacao/codigo_obras.html')


from django.shortcuts import render

def uso_solo_view(request):
    return render(request, 'legislacao/uso_solo.html')


# webproject/webapp/views.py
from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm

def noticia_nova(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias_listar')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/form.html', {'form': form})



def servico_novo(request):
    return render(request, 'servicos/form.html')  # ou o template correto para o formulário



@login_required
def dashboard_view(request):
    return render(request, 'webapp/dashboard.html')  # template agora existe
