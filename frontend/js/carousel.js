// Minimal JavaScript to make arrow buttons scroll the carousel container
window.addEventListener('DOMContentLoaded', () => {
    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');
    const carouselContainer = document.querySelector('.carousel-container');
  
    // Amount to scroll horizontally each click (in pixels)
    const scrollAmount = 300;
  
    leftArrow.addEventListener('click', () => {
      carouselContainer.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth'
      });
    });
  
    rightArrow.addEventListener('click', () => {
      carouselContainer.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
      });
    });
  });
  