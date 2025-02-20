// Minimal JS for arrow-based scrolling
window.addEventListener('DOMContentLoaded', () => {
    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');
    const carouselContainer = document.querySelector('.carousel-container');
  
    // Amount to scroll horizontally each click
    const scrollAmount = 300;
  
    leftArrow.addEventListener('click', () => {
      carouselContainer.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth',
      });
    });
  
    rightArrow.addEventListener('click', () => {
      carouselContainer.scrollBy({
        left: scrollAmount,
        behavior: 'smooth',
      });
    });
  });
  