// Carrossel
document.querySelectorAll('.carrossel-container').forEach(container => {
    const carrossel = container.querySelector('.carrossel');
    const jogos = carrossel.children.length;
    let index = 0;

    container.querySelector('.seta.direita').addEventListener('click', () => {
        index = (index + 1) % jogos;
        carrossel.style.transform = `translateX(${-index * (100 / jogos)}%)`;
    });

    container.querySelector('.seta.esquerda').addEventListener('click', () => {
        index = (index - 1 + jogos) % jogos;
        carrossel.style.transform = `translateX(${-index * (100 / jogos)}%)`;
    });
});

// Função para alternar a visibilidade do menu
function toggleMenu() {
    var menu = document.getElementById('menu');  // Pegando o elemento do menu
    if (menu.style.display === "block") {
        menu.style.display = "none";  // Se o menu estiver visível, esconde
    } else {
        menu.style.display = "block";  // Se o menu estiver escondido, exibe
    }
}

// Redirecionar para perfil
function goToProfile() {
    window.location.href = "configuracao.html";
}

// Corrigir redirecionamento do menu
function redirecionar(url) {
    const menu = document.getElementById('menu');
    menu.classList.remove('active'); // Fecha o menu
    window.location.href = url;
}

// Salvar time favorito
function salvarTimeFavorito() {
    var timeFavorito = document.getElementById('timeFavorito').value;
    if (timeFavorito) {
        localStorage.setItem('timeFavorito', timeFavorito); // Salva no localStorage
        alert('Seu time favorito é: ' + timeFavorito.charAt(0).toUpperCase() + timeFavorito.slice(1));
    } else {
        alert('Por favor, selecione um time favorito.');
    }
}

// Adiciona um evento ao botão para exibir a imagem da tabela
document.getElementById("mostrarClassificacao").addEventListener("click", function() {
    const campeonato = document.getElementById("campeonatos").value;
    const tabelaImagem = document.getElementById("tabelaImagem");

    if (campeonato) {
        const imagemPath = `img/${campeonato}.png`; // Caminho da imagem

        tabelaImagem.src = imagemPath;  // Define a imagem a ser exibida

        // Exibe uma imagem de carregamento ou uma barra de progresso (opcional)
        tabelaImagem.style.display = "none"; // Inicialmente oculta até carregar a imagem

        // Espera a imagem carregar corretamente
        const img = new Image();
        img.src = imagemPath;

        img.onload = function() {
            // Sucesso ao carregar
            tabelaImagem.src = imagemPath;  // Atualiza a imagem a ser exibida
            tabelaImagem.style.display = "block";  // Exibe a imagem
            console.log("Imagem carregada com sucesso.");
        };

        img.onerror = function() {
            // Erro ao carregar a imagem
            console.error(`Erro ao carregar a tabela. Verifique se a imagem ${campeonato}.png existe na pasta img.`);
            alert("Erro ao carregar a tabela. Verifique o arquivo de imagem.");
            tabelaImagem.style.display = "none";  // Esconde a imagem caso ocorra erro
        };
    } else {
        alert("Por favor, selecione um campeonato!");
        tabelaImagem.style.display = "none";  // Esconde a imagem caso não tenha campeonato selecionado
    }
});

function mostrarResultados() {
    const selecionado = document.getElementById('campeonato').value;
    const tabelas = document.querySelectorAll('.tabela-container');

    tabelas.forEach(tabela => {
        tabela.style.display = 'none'; // Esconde todas as tabelas
    });

    if (selecionado) {
        document.getElementById(selecionado).style.display = 'block'; // Mostra a tabela selecionada
    }
}

