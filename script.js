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


function toggleMenu() {
    const menu = document.getElementById('menu');
    // Alterna a classe 'active' para mostrar ou esconder o menu
    menu.classList.toggle('active');
    // Alterna entre 'block' e 'none' para mostrar ou esconder o menu
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block'; 
}

// Função para redirecionar para a página de perfil
function goToProfile() {
    window.location.href = "configuracao.html"; // Redireciona para a página de configuração
}

// Corrigindo a função para redirecionamento do menu
function redirecionar(url) {
    const menu = document.getElementById('menu');
    menu.style.display = 'none'; // Fecha o menu ao clicar
    window.location.href = url; // Redireciona para a URL
}

// A função de salvar time favorito
function salvarTimeFavorito() {
    var timeFavorito = document.getElementById('timeFavorito').value;
    if (timeFavorito) {
        alert('Seu time favorito é: ' + timeFavorito.charAt(0).toUpperCase() + timeFavorito.slice(1));
    } else {
        alert('Por favor, selecione um time favorito.');
    }
}

document.getElementById("mostrarClassificacao").addEventListener("click", function() {
    const campeonato = document.getElementById("campeonatos").value;
    
    if (campeonato) {
        const tabelaImagem = document.getElementById("tabelaImagem");
        tabelaImagem.src = `img/${campeonato}.png`;  // Mudando para .png

        tabelaImagem.onload = function() {
            tabelaImagem.classList.add('show');  /* Exibe a imagem quando carregada */
        };

        tabelaImagem.onerror = function() {
            alert("Erro ao carregar a tabela. Verifique o arquivo de imagem.");
        };
    } else {
        alert("Por favor, selecione um campeonato!");
    }
});

// resultado 

document.getElementById("mostrarResultados").addEventListener("click", function() {
    const campeonato = document.getElementById("campeonatoResultados").value;
    const resultadosContainer = document.getElementById("resultados");
    
    // Limpa resultados anteriores
    resultadosContainer.innerHTML = "";

    if (campeonato && resultadosDosJogos[campeonato]) {
        resultadosDosJogos[campeonato].forEach(jogo => {
            const jogoDiv = document.createElement("div");
            jogoDiv.classList.add("jogo");

            // Estrutura HTML para exibir escudo, placar e nome dos times
            jogoDiv.innerHTML = `
                <img src="img/${jogo.time1}.png" alt="${jogo.time1}" class="escudo">
                <span class="placar">${jogo.placar}</span>
                <img src="img/${jogo.time2}.png" alt="${jogo.time2}" class="escudo">
            `;

            resultadosContainer.appendChild(jogoDiv);
        });
    } else {
        alert("Por favor, selecione um campeonato válido!");
    }
});