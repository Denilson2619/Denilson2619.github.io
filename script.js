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

<<<<<<< HEAD
document.querySelector('.menu-icon').addEventListener('click', function() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
});

function toggleMenu() {
    const sidebar = document.getElementById("sidebarMenu");
    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";
        sidebar.style.display = "none";
    } else {
        sidebar.style.width = "250px";
        sidebar.style.display = "block";
    }
}
=======

>>>>>>> b34da5e259230fd3058906f8aa5bf4fdf5e2db87
