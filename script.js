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

document.getElementById("mostrarClassificacao").addEventListener("click", function() {
    const campeonato = document.getElementById("campeonatos").value;
    
    if (campeonato) {
        const tabelaImagem = document.getElementById("tabelaImagem");
        tabelaImagem.src = `img/${campeonato}.png`;  // Isso irá gerar algo como img/brasileiro.png

        // Log para verificar o caminho da imagem
        console.log(`Tentando carregar a imagem: img/${campeonato}.png`);

        // Exibe a imagem enquanto ela está carregando
        tabelaImagem.style.display = "block";

        tabelaImagem.onload = function() {
            tabelaImagem.classList.add('show');  /* Exibe a imagem quando carregada */
            tabelaImagem.style.opacity = 1;
        };
        
        tabelaImagem.onerror = function() {
            console.error(`Erro ao carregar a tabela. Caminho tentado: img/${campeonato}.png`);
            alert("Erro ao carregar a tabela. Verifique o arquivo de imagem.");
            tabelaImagem.style.display = "none"; // Esconde a imagem caso ocorra erro
        };
    } else {
        alert("Por favor, selecione um campeonato!");
        const tabelaImagem = document.getElementById("tabelaImagem");
        tabelaImagem.style.display = "none"; // Esconde a imagem caso não tenha campeonato selecionado
    }
});

// Exibir resultados
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