// JavaScript para mover el carrusel manualmente
let currentIndex = 0;

function moveCarousel(direction) {
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;

    if (direction === 'next') {
        currentIndex = (currentIndex + 1) % totalItems;
    } else if (direction === 'prev') {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems;
    }

    const carouselContainer = document.querySelector('.carousel-container');
    const offset = -currentIndex * 100; // Mueve el carrusel por el ancho de un item
    carouselContainer.style.transform = `translateX(${offset}%)`;
}
