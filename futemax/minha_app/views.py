from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from minha_app.models import CustomUser
from django.shortcuts import render


# Create your views here.



def index_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verificar se o usuário existe e autenticar
        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect("index")  # Redireciona para a página inicial após login bem-sucedido
        else:
            messages.error(request, "E-mail ou senha incorretos.")
            return redirect("index")  # Redireciona para a página de login

    return render(request, "index")  # Renderiza o template de login



def cadastro_view(request):
    if request.method == "POST":
        username = request.POST['username']  # Agora você está capturando o 'username'
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirma_senha = request.POST['confirma_senha']

        # Verificar se as senhas coincidem
        if senha == confirma_senha:
            # Criar o usuário com o nome de usuário
            user = CustomUser.objects.create_user(
                username=username,
                nome=nome,
                email=email,
                password=senha
            )
            user.save()
            return redirect('index')  # Redirecionar para a página de login
        else:
            # Se as senhas não coincidirem
            return render(request, 'cadastro', {'error': 'As senhas não coincidem.'})

    return render(request, 'cadastro')


def modelo_view(request):
    return render(request, 'modelo.html')

def classificacao_view(request):
    # Dados simulados das tabelas de classificação por campeonato
    tabelas = {
        "brasileiro": {
            "imagem": "img/tabela_brasileirao.png",
            "descricao": "Tabela de Classificação do Brasileirão",
        },
        "champions": {
            "imagem": "img/tabela_champions.png",
            "descricao": "Tabela de Classificação da Champions League",
        },
    }

    campeonato_selecionado = request.GET.get("campeonato", None)

    # Obtém a tabela correspondente, se disponível
    tabela = tabelas.get(campeonato_selecionado, None)

    return render(
        request,
        "classificacao",
        {"tabela": tabela, "campeonato_selecionado": campeonato_selecionado},
    )


def iniciar_view(request):
    # Dados simulados para exibição dinâmica
    jogos = {
        "Brasileirao": [
            {"imagem": "img/FLAvsVAS.png", "link": "melhores_momentos_flaxvas.html", "descricao": "Flamengo x Vasco"},
            {"imagem": "img/SÃOvsCOR.png", "link": "melhores_momentos_saoxcor.html", "descricao": "São Paulo x Corinthians"},
            {"imagem": "img/CRIvsCAP.png", "link": "melhores_momentos_crixcap.html", "descricao": "Criciúma x CAP"},
            {"imagem": "img/RBBvsPLA.png", "link": "melhores_momentos_rbbvspla.html", "descricao": "Red Bull Bragantino x Palmeiras"},
            {"imagem": "img/botxflu.png", "link": "melhores_momentos_botxflu.html", "descricao": "Botafogo x Fluminense"},
        ],
        "Epicos": [
            {"imagem": "img/cityxreal.png", "link": "melhores_momentos_cityxreal.html", "descricao": "Manchester City x Real Madrid"},
            {"imagem": "img/barcaxpsg.png", "link": "melhores_momentos_barcaxpsg.html", "descricao": "Barcelona x PSG"},
            {"imagem": "img/braxita.png", "link": "melhores_momentos_braxita.html", "descricao": "Brasil x Itália"},
            {"imagem": "img/argxfra.png", "link": "melhores_momentos_argxfra.html", "descricao": "Argentina x França"},
        ],
        "ChampionsLeague": [
            {"imagem": "img/bayerXarsenal.png", "link": "melhores_momentos_bayerxarsenal.html", "descricao": "Bayer Munique x Arsenal"},
            {"imagem": "img/barçaXmonaco.png", "link": "melhores_momentos_barcaxmonaco.html", "descricao": "Barcelona x Monaco"},
            {"imagem": "img/realXmilan.png", "link": "melhores_momentos_realxmilan.html", "descricao": "Real Madrid x Milan"},
        ],
    }

    return render(request, "iniciar.html", {"jogos": jogos})



def redefinir_senha_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # Simulação: Verificar se o e-mail existe no sistema (normalmente integrado ao banco de dados)
        usuario_existe = verificar_email_no_sistema(email)

        if usuario_existe:
            # Simular envio de e-mail (configurar no settings.py para ambiente real)
            send_mail(
                subject="Redefinição de senha",
                message="Clique no link para redefinir sua senha: <link_fake_para_redefinicao>",
                from_email="noreply@futmax.com",
                recipient_list=[email],
            )

        # Exibir mensagem genérica de confirmação
        return render(request, "processar_redefinicao.html")
    else:
        # Redirecionar para página inicial se a rota for acessada diretamente
        messages.error(request, "Ação inválida.")
        return redirect("login")


def verificar_email_no_sistema(email):
    # Substituir por lógica real de consulta ao banco de dados
    emails_cadastrados = ["usuario1@example.com", "usuario2@example.com"]  # Exemplo
    return email in emails_cadastrados

def processar_redefinicao_view(request):
    return render(request, 'processar-redefinicao.html')

def resultados_view(request):
    # Dados simulados para os resultados
    resultados = {
        "brasileirao": [
            {"time1": "Vasco", "placar": "0x2", "time2": "Flamengo", "escudos": ["img/logo-vasco-da-gama-1024.png", "img/Flamengo_braz_logo.svg.png"]},
            {"time1": "São Paulo", "placar": "2x2", "time2": "Corinthians", "escudos": ["img/logo-sao-paulo-1024.png", "img/Corinthianssccp2023.png"]},
            {"time1": "Criciúma", "placar": "2x2", "time2": "Athletico-PR", "escudos": ["img/EscudoCriciumaEC.svg.png", "img/Club_Athletico_Paranaense_2019.png"]},
        ],
        "champions": [
            {"time1": "Bayern", "placar": "0x2", "time2": "Arsenal", "escudos": ["img/bayern-munchen-1024.png", "img/arsenal-football-club-1024.png"]},
            {"time1": "Barcelona", "placar": "2x2", "time2": "Monaco", "escudos": ["img/logo-barcelona-1024.png", "img/as-monaco-1024.png"]},
            {"time1": "Milan", "placar": "2x2", "time2": "Real Madrid", "escudos": ["img/associazione-calcio-milan-1024.png", "img/logo-real-madrid-escudo-1024.png"]},
        ],
        "epicos": [
            {"time1": "Real Madrid", "placar": "3x3", "time2": "Man City", "escudos": ["img/logo-real-madrid-escudo-1024.png", "img/manchester-city-football-club-1024.png"]},
            {"time1": "Barcelona", "placar": "6x1", "time2": "PSG", "escudos": ["img/logo-barcelona-1024.png", "img/paris-saint-germain-1024.png"]},
            {"time1": "Brasil", "placar": "(3)0x0(2)", "time2": "Itália", "escudos": ["img/logo-selecao-brasileira-brasil-novo-logo-2019-com-estrelas-e-nome-256.png", "img/logoitalia.png"]},
        ],
    }

    campeonato_selecionado = request.GET.get("campeonato", None)
    jogos = resultados.get(campeonato_selecionado, [])

    return render(
        request,
        "resultados.html",
        {
            "jogos": jogos,
            "campeonato_selecionado": campeonato_selecionado,
        },
    )