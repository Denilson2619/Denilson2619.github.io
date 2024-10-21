// Função para o carrossel do Brasileirão
const carrosselBrasileirao = document.getElementById('carrosselBrasileirao');
let scrollPosBrasileirao = 0;

document.getElementById('nextBrasileirao').addEventListener('click', function () {
    scrollPosBrasileirao -= 200;  // Ajuste o valor conforme necessário
    carrosselBrasileirao.style.transform = `translateX(${scrollPosBrasileirao}px)`;
});

document.getElementById('prevBrasileirao').addEventListener('click', function () {
    scrollPosBrasileirao += 200;  // Ajuste o valor conforme necessário
    carrosselBrasileirao.style.transform = `translateX(${scrollPosBrasileirao}px)`;
});

// Função para o carrossel da Arábia Saudita
const carrosselArabiaSaudita = document.getElementById('carrosselArabiaSaudita');
let scrollPosArabiaSaudita = 0;

document.getElementById('nextArabiaSaudita').addEventListener('click', function () {
    scrollPosArabiaSaudita -= 200;  // Ajuste o valor conforme necessário
    carrosselArabiaSaudita.style.transform = `translateX(${scrollPosArabiaSaudita}px)`;
});

document.getElementById('prevArabiaSaudita').addEventListener('click', function () {
    scrollPosArabiaSaudita += 200;  // Ajuste o valor conforme necessário
    carrosselArabiaSaudita.style.transform = `translateX(${scrollPosArabiaSaudita}px)`;
});

// Função para o carrossel da Champions
const carrosselChampions = document.getElementById('carrosselChampions');
let scrollPosChampions = 0;

document.getElementById('nextChampions').addEventListener('click', function () {
    scrollPosChampions -= 200;  // Ajuste o valor conforme necessário
    carrosselChampions.style.transform = `translateX(${scrollPosChampions}px)`;
});

document.getElementById('prevChampions').addEventListener('click', function () {
    scrollPosChampions += 200;  // Ajuste o valor conforme necessário
    carrosselChampions.style.transform = `translateX(${scrollPosChampions}px)`;
});

