const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  })

  document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
  }))

  var currentSlide = 1;
  var totalSlides = document.querySelectorAll('.slider img').length;

  function prevSlide() {
    if (currentSlide === 1) {
      currentSlide = totalSlides;
    } else {
      currentSlide--;
    }
    showSlide(currentSlide);
  }

  function nextSlide() {
    if (currentSlide === totalSlides) {
      currentSlide = 1;
    } else {
      currentSlide++;
    }
    showSlide(currentSlide);
  }

  function showSlide(slideNumber) {
    var slides = document.querySelectorAll('.slider img');
    for (var i = 0; i < slides.length; i++) {
      slides[i].style.display = 'none';
    }
    slides[slideNumber - 1].style.display = 'block';
  }