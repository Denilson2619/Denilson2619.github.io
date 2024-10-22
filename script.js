const carrosselBrasileirao = document.getElementById('carrosselBrasileirao');
const prevBrasileirao = document.getElementById('prevBrasileirao');
const nextBrasileirao = document.getElementById('nextBrasileirao');
let currentSlide = 0;

function showOrHideSetas() {
    // Verifica se a seta esquerda deve estar visível
    if (currentSlide === 0) {
        prevBrasileirao.classList.add('inativa');
    } else {
        prevBrasileirao.classList.remove('inativa');
    }

    // Verifica se a seta direita deve estar visível
    if (currentSlide >= carrosselBrasileirao.children.length - 5) {
        nextBrasileirao.classList.add('inativa');
    } else {
        nextBrasileirao.classList.remove('inativa');
    }
}

nextBrasileirao.addEventListener('click', () => {
    if (currentSlide < carrosselBrasileirao.children.length - 5) {
        currentSlide++;
        carrosselBrasileirao.style.transform = `translateX(-${currentSlide * 20}%)`;
        showOrHideSetas();
    }
});

prevBrasileirao.addEventListener('click', () => {
    if (currentSlide > 0) {
        currentSlide--;
        carrosselBrasileirao.style.transform = `translateX(-${currentSlide * 20}%)`;
        showOrHideSetas();
    }
});

showOrHideSetas();


