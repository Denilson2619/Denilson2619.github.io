document.querySelectorAll('.carrossel-container').forEach(container => {
    const carrossel = container.querySelector('.carrossel');
    const jogos = carrossel.children.length;
    let index = 0;

    container.querySelector('.seta.direita').addEventListener('click', () => {
        index = (index + 1) % jogos; // Incrementa o índice
        carrossel.style.transform = `translateX(${-index * (100 / jogos)}%)`; // Move o carrossel para a esquerda
    });

    container.querySelector('.seta.esquerda').addEventListener('click', () => {
        index = (index - 1 + jogos) % jogos; // Decrementa o índice
        carrossel.style.transform = `translateX(${-index * (100 / jogos)}%)`; // Move o carrossel para a direita
    });
});

function mostrarClassificacao() {
    const campeonato = document.getElementById('campeonatos').value;
    const imgTabela = document.getElementById('tabelaImagem');

    // Mapeamento de campeonatos para suas respectivas imagens
    const imagens = {
        'brasileirao': 'img/brasileiro.png',
        'champions': 'img/champions.png', // Coloque o caminho correto da imagem da Champions
        'arabia': 'img/arabia.png' // Coloque o caminho correto da imagem da Arábia Saudita
    };

    // Verifica se o campeonato selecionado tem uma imagem
    if (imagens[campeonato]) {
        imgTabela.src = imagens[campeonato]; // Define o src da imagem
        imgTabela.style.display = 'block'; // Exibe a imagem
    } else {
        imgTabela.src = ''; // Limpa o src se não houver seleção
        imgTabela.style.display = 'none'; // Oculta a imagem
    };

    mostrarResultados(); // Chama a função para mostrar resultados
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('campeonato').addEventListener('change', mostrarResultados);
});

function mostrarResultados() {
    const campeonato = document.getElementById('campeonato').value;
    const tabelas = document.querySelectorAll('.tabela-resultados');

    // Ocultar todas as tabelas de resultados
    tabelas.forEach(tabela => {
        tabela.style.display = 'none';
    });

    // Mostrar a tabela correspondente ao campeonato selecionado
    const tabelaSelecionada = document.querySelector(`.tabela-${campeonato}`);
    if (tabelaSelecionada) {
        tabelaSelecionada.style.display = 'block'; // Exibe a tabela selecionada
    }
}

function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block'; // Alterna a exibição do menu
}

function goToProfile() {
    window.location.href = "configuracao.html";
}



document.getElementById('mostrarClassificacao').addEventListener('click', mostrarClassificacao);

function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block'; // Alterna a exibição do menu
}

// Nova função para redirecionar e fechar o menu
function redirecionar(url) {
    const menu = document.getElementById('menu');
    menu.style.display = 'none'; // Fecha o menu ao clicar
    window.location.href = url; // Redireciona para a URL
}

function salvarTimeFavorito() {
    // Captura o valor selecionado no dropdown
    var timeFavorito = document.getElementById('timeFavorito').value;

    // Verifica se o usuário selecionou um time
    if (timeFavorito) {
        // Exibe uma mensagem personalizada com o nome do time
        alert('Seu time favorito é: ' + timeFavorito.charAt(0).toUpperCase() + timeFavorito.slice(1));
    } else {
        // Caso não tenha selecionado, avisa o usuário
        alert('Por favor, selecione um time favorito.');
    }
}

function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.classList.toggle('active');
}

function goToProfile() {
    window.location.href = "configuracao.html";
}