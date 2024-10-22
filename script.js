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

document.getElementById('mostrarClassificacao').addEventListener('click', () => {
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
    }
});