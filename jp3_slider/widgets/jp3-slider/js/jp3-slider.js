  svgcircle1 = document.getElementById('circle1');

  
  if (svgcircle1){

    pathscircle1 = svgcircle1.getElementsByTagName("path");
  }
  
  svgcircle2 = document.getElementById('circle2');

  if (svgcircle2) {
    pathscircle2 = svgcircle2.getElementsByTagName("path");
  }
  
  
svgcircle3 = document.getElementById('circle3');

if (svgcircle3){

  pathscircle3 = svgcircle3.getElementsByTagName("path");
}

const about_text = document.querySelectorAll(".about__container__right__text");
const about_text_parapgraph = document.querySelector('.about__container__right__text__paragraph')
const patchwork_second_img = [...document.querySelectorAll(".second_patchwork > img")];

const first_text = document.querySelector(".js__1__text");
const second_text = document.querySelector(".js__2__text");
const third_text = document.querySelector(".js__3__text");

const first_button = document.querySelector(".js__1__button");
const second_button = document.querySelector(".js__2__button");
const third_button = document.querySelector(".js__3__button");

gsap.set(patchwork_second_img, {
  y:0,
});

patchwork_second_img.forEach((content, i) => {
  gsap.to(content, {
    y:-450,
    ease:'power4.easeInOut',
    scrollTrigger: {
      trigger: content,
      scroller: "body",
      start: "top 100%",
      end: "top -10%",
      scrub: true,
    }
  });
});

gsap.timeline({
  scrollTrigger: {
    trigger: about_text,
    start: "center center",
    end: "center 85%",
    endTrigger: ".elements__end",
    scroller: "body",
    scrub: true,
    pin: true,
  }
});

if (svgcircle1 && pathscircle1 ){


gsap.set(pathscircle1, {
  drawSVG: "0% 0%"
});

gsap.to(pathscircle1, {
  drawSVG: "0% 100%",
  scrollTrigger: {
    scroller: "body",
    trigger: ".circle__1",
    start: "top center",
    end: "top -30%",
    scrub:true,
  }
});

}

if (svgcircle2 && pathscircle2 ){

gsap.set(pathscircle2, {
  drawSVG: "0% 0%"
});

gsap.to(pathscircle2, {
  drawSVG: "0% 100%",
  scrollTrigger: {
    scroller: "body",
    trigger: ".circle__2",
    start: "top 65%",
    end: "top -15%",
    scrub:true,
  }
});
}

if (svgcircle3 && pathscircle3 ){

  gsap.set(pathscircle3, {
    drawSVG: "0% 0%"
  });
  
  gsap.to(pathscircle3, {
    drawSVG: "0% 100%",
    scrollTrigger: {
      scroller: "body",
      trigger: ".circle__3",
      start: "top 86.5%",
      end: "top 25%",
      scrub:true,
    }
  });
}

if (first_text){

  
  gsap.to(first_text, {
    scrollTrigger: {
      trigger: ".circle__1",
      scroller: "body",
      start: "top 120%",
      end: "top -10%",
      onEnter: () => {add__first__text() ,resize_paragraph(first_text)}, 
      onLeave: () => remove__first__text(),
      onEnterBack: () => {add__first__text() ,resize_paragraph(first_text)}, 
      onLeaveBack: () => remove__first__text(),
    }
  });
}

if (second_text){
  
  gsap.to(second_text, {
    scrollTrigger: {
      trigger: ".circle__2",
      scroller: "body",
      start: "top 85%",
      end: "top -10%",
      onEnter: () => {add__second__text() ,resize_paragraph(second_text)}, 
      onLeave: () => remove__second__text(),
      onEnterBack: () => {add__second__text() ,resize_paragraph(second_text)},
      onLeaveBack: () => remove__second__text(),
    }
  });
}
if (third_text ){

gsap.to(third_text, {
  scrollTrigger: {
    trigger: ".circle__3",
    scroller: "body",
    start: "top 85%",
    end: "top -55%",
    onEnter: () => {add__third__text(), resize_paragraph(third_text)},
    onLeave: () => remove__third__text(),
    onEnterBack: () => {add__third__text(), resize_paragraph(third_text)},
    onLeaveBack: () => remove__third__text(),
  }
});
}

function add__first__text() {
  first_text.classList.add('text__active')
  first_button.classList.add('text__active')
}

function remove__first__text() {
  first_text.classList.remove('text__active')
  first_button.classList.remove('text__active')
}

function add__second__text() {
  second_text.classList.add('text__active')
  second_button.classList.add('text__active')
}

function remove__second__text() {
  second_text.classList.remove('text__active')
  second_button.classList.remove('text__active')
}

function add__third__text() {
  third_text.classList.add('text__active')
  third_button.classList.add('text__active')
}

function remove__third__text() {
  third_text.classList.remove('text__active')
  third_button.classList.remove('text__active')
}
function resize_paragraph(element){
  about_text_parapgraph.style.height = `${element.clientHeight}px`
  console.log(element.clientHeight)
}

////////////////////////////////////////////////////////////////////// SWIPER CAROUSEL FOR CUSTOM SLIDER////////////////////////////////////////////////////////////////////
if (window.matchMedia("(max-width: 992px)").matches) {
var swiperabout = new Swiper(".swiper-container_about", {
  spaceBetween: 30,
  centeredSlides: true,
  // initialSlide: 0,
  // effect: "fade",
  // slidesPerView: 0,
  // slidesPerGroup: 1,
  // spaceBetween: 60,
  loop:true,
  // speed:200,
  // loopFillGroupWithBlank: true,
  navigation: {
    nextEl: '.swiper-button-next-svg',
    prevEl: '.swiper-button-prev-svg',
  },
  // autoplay: {
  //   delay: 7000,
  //   disableOnInteraction: false,
  // },
});


swiperabout.on('slideChange', function()  {


  const slide_visible_about = document.querySelectorAll('.swiper-slide_about');

  const activeElSlide = Array.prototype.find.call (slide_visible_about, item => item.classList.contains('swiper-slide-active'));

  const idActiveSlide = activeElSlide.getAttribute('data-id');

  const slide_visible_text = document.querySelectorAll('.slide__text__id');

  const slide_visible_button = document.querySelectorAll('.slide__button__id');

  

  slide_visible_text.forEach((element) => {
    const slideVisibleTextEl = element.getAttribute('data-id');
    if (idActiveSlide === slideVisibleTextEl) {
      element.classList.add('text__active');
    } else {
      element.classList.remove('text__active');
    }
  });

  slide_visible_button.forEach((element) => {
    const slideVisibleButtonEl = element.getAttribute('data-id');
    if (idActiveSlide === slideVisibleButtonEl) {
      element.classList.add('text__active');
    } else {
      element.classList.remove('text__active');
    }
  });
});

const swiperAboutSlide = document.querySelector('.swiper-container_about')
swiperAboutSlide.addEventListener('mouseenter', function() {
  swiperabout.autoplay.stop();
});

swiperAboutSlide.addEventListener('mouseleave', function() {
  swiperabout.autoplay.start();
});

} else {
  console.log('disable slider');
}



