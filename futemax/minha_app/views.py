from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from minha_app.models import CustomUser
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def index_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verificar se o usuário existe e autenticar
        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect("iniciar.html")  # Redireciona para a página inicial após login bem-sucedido
        else:
            messages.error(request, "E-mail ou senha incorretos.")
            return redirect("index.html")  # Redireciona para a página de login

    return render(request, "iniciar.html")  # Renderiza o template de login





def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        email = request.POST['email']
        confirma_senha = request.POST.get('confirma_Senha')  # Retorna None se a chave não existir

        # Verificar se as senhas coincidem
        if password == confirma_senha:
            # Criar o usuário com o nome de usuário
            user = CustomUser.objects.create_user(
                nome=username,
                email=email,
                password=password,
                
            )
            user.save()
            return redirect('index.html')  # Redirecionar para a página de login
        else:
            # Se as senhas não coincidirem
            return render(request, 'cadastro.html', {'error': 'As senhas não coincidem.'})

    return render(request, 'cadastro.html')


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

    return render(request,"classificacao.html",
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
            {"time1": "Red Bull Bragantino", "placar": "3x1", "time2": "Palmeiras", "escudos": ["img/RedBullBragantino.png", "img/palmeiras.png"]},
            {"time1": "Fluminense", "placar": "3x1", "time2": "Botafogo", "escudos": ["img/flumin.svg", "img/Botafogo_de_Futebol_e_Regatas_logo.svg.png"]},
            {"time1": "Atlético Goianiense", "placar": "0x0", "time2": "Cuiabá", "escudos": ["img/Atlético_Goianiense.svg.png", "img/CuiabáEC2020.png"]},
            {"time1": "Internacional", "placar": "3x1", "time2": "Grêmio", "escudos": ["img/Scinternacional1909.png", "img/logo-gremio-1024.png"]},
            {"time1": "Fortaleza", "placar": "3x1", "time2": "Atlético Mineiro", "escudos": ["img/Fortaleza_EC_2018.png", "img/800px-Atletico_mineiro_galo.png"]},
            {"time1": "Cruzeiro", "placar": "3x1", "time2": "Bahia", "escudos": ["img/Cruzeiro_Esporte_Clube_(logo).svg", "img/logo-bahia-1024.png"]},
        ],
        "champions": [
            {"time1": "Bayern", "placar": "0x2", "time2": "Arsenal", "escudos": ["img/bayern-munchen-1024.png", "img/arsenal-football-club-1024.png"]},
            {"time1": "Barcelona", "placar": "2x2", "time2": "Monaco", "escudos": ["img/logo-barcelona-1024.png", "img/as-monaco-1024.png"]},
            {"time1": "Milan", "placar": "2x2", "time2": "Real Madrid", "escudos": ["img/associazione-calcio-milan-1024.png", "img/logo-real-madrid-escudo-1024.png"]},
            {"time1": "Benfica", "placar": "3x1", "time2": "Atlético Madrid", "escudos": ["img/logo-benfica-2.png", "img/logo-atletico-madrid-1536.png"]},
            {"time1": "PSG", "placar": "0x0", "time2": "PSV Eindhoven", "escudos": ["img/paris-saint-germain-1024.png", "img/logo-psv-eindhoven-2.png"]},
            {"time1": "Liverpool", "placar": "3x1", "time2": "Bayer Leverkusen", "escudos": ["img/liverpool-football-club-256.png", "img/bayer-04-leverkusen-256.png"]},
            {"time1": "RB Leipzig", "placar": "3x1", "time2": "Juventus", "escudos": ["img/rb-leipzig-256.png", "img/juventus-football-club-256.png"]},
            {"time1": "Manchester City", "placar": "3x1", "time2": "Internazionale", "escudos": ["img/manchester-city-football-club-1024.png", "img/football-club-internazionale-milano-256.png"]},
            {"time1": "Club Brugge", "placar": "3x1", "time2": "Aston Villa", "escudos": ["img/logo-brugge-5.png", "img/Aston_Villa_F.C._Logo_2023.png"]},
        ],

        "epicos": [
            {"time1": "Real Madrid", "placar": "3x3", "time2": "Man City", "escudos": ["img/logo-real-madrid-escudo-1024.png", "img/manchester-city-football-club-1024.png"]},
            {"time1": "Barcelona", "placar": "6x1", "time2": "PSG", "escudos": ["img/logo-barcelona-1024.png", "img/paris-saint-germain-1024.png"]},
            {"time1": "Brasil", "placar": "(3)0x0(2)", "time2": "Itália", "escudos": ["img/logo-selecao-brasileira-brasil-novo-logo-2019-com-estrelas-e-nome-256.png", "img/logoitalia.png"]},
            {"time1": "Argentina", "placar": "(4)3x3(2)", "time2": "França", "escudos": ["img/selecao-argentina-de-futebol-256.png", "img/selecao-francesa-de-futebol-256.png"]},
            {"time1": "Flamengo", "placar": "5x4", "time2": "Santos", "escudos": ["img/Flamengo_braz_logo.svg.png", "img/logo-santos-256.png"]},
            {"time1": "Corinthians", "placar": "1x0", "time2": "Chelsea", "escudos": ["img/Corinthianssccp2023.png", "img/chelsea-football-club-256.png"]},
            {"time1": "Tottenham", "placar": "3x2", "time2": "Ajax", "escudos": ["img/tottenham-hotspur-football-club-256.png", "img/logo-ajax-5.png"]},
            {"time1": "São Paulo", "placar": "1x0", "time2": "Liverpool", "escudos": ["img/logo-sao-paulo-1024.png", "img/liverpool-football-club-256.png"]},
            {"time1": "Manchester United", "placar": "3x2", "time2": "Milan", "escudos": ["img/manchester-united-football-club-4096.png", "img/associazione-calcio-milan-1024.png"]},
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

