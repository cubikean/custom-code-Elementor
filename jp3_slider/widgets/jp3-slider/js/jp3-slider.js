

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
    start: "center 40%",
    end: "center bottom",
    endTrigger: ".elements__end",
    scroller: "body",
    scrub: true,
    pin: true,
  }
});

function animatePath(pathCircle, triggerClass, start, end) {
  if (pathCircle) {
    gsap.set(pathCircle, {
      drawSVG: "0% 0%"
    });
    
    gsap.to(pathCircle, {
      drawSVG: "0% 100%",
      scrollTrigger: {
        scroller: "body",
        trigger: triggerClass,
        start: start,
        end: end,
        scrub: true,
      }
    });
  }
}

const pathscircle1 = document.querySelector('#circle1 path')
const pathscircle2 = document.querySelector('#circle2 path')
const pathscircle3 = document.querySelector('#circle3 path')

animatePath(pathscircle1, ".circle__1", "top center", "top -30%");
animatePath(pathscircle2, ".circle__2", "top 65%", "top -15%");
animatePath(pathscircle3, ".circle__3", "top 86.5%", "top 25%");


function animateText(text, circleClass, start, end, index) {
  gsap.to(text, {
    scrollTrigger: {
      trigger: circleClass,
      scroller: "body",
      start: start,
      end: end,
      onEnter: () => {addText(text, index), resizeParagraph(text), colorTitle(index)},
      onLeave: () => {removeText(text, index), removeColorTitle(index)},
      onEnterBack: () => {addText(text, index), resizeParagraph(text), colorTitle(index)},
      onLeaveBack: () => {removeText(text, index), removeColorTitle(index)},
    }
  });
}

if (first_text) {
  animateText(first_text, ".circle__1",  "top 120%", "top -10%", 1);
}

if (second_text) {
  animateText(second_text, ".circle__2", "top 70%", "top -10%", 2);
}

if (third_text) {
  animateText(third_text, ".circle__3", "top 85%", "top -55%", 3);
}

function addText(text, index) {
  text.classList.add('text__active')
  document.querySelector(`.js__${index}__button`).classList.add('text__active')
}

function removeText(text, index) {
  console.log('leave')
  text.classList.remove('text__active')
  document.querySelector(`.js__${index}__button`).classList.remove('text__active')
}

function resizeParagraph(element){
  about_text_parapgraph.style.height = `${element.clientHeight}px`
}

function colorTitle(id){
  const currentId = document.querySelector(`[data-title-id="${id}"] a`)
  if (currentId){
    currentId.style.color = 'var(--orange)';
    currentId.classList.add('active')
  }
}

function removeColorTitle(id){
  const currentId = document.querySelector(`[data-title-id="${id}"] a`)
  if (currentId){
    currentId.style.color = '#DBDBDB';
    currentId.classList.remove('active')
  }
}

////////////////////////////////////////////////////////////////////// SWIPER CAROUSEL FOR CUSTOM SLIDER////////////////////////////////////////////////////////////////////
if (window.matchMedia("(max-width: 992px)").matches) {
var swiperabout = new Swiper(".swiper-container_about", {
  spaceBetween: 30,
  // centeredSlides: true,
  // initialSlide: 0,
  // effect: "fade",
  // slidesPerView: 1,
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


// swiperabout.on('slideChange', function()  {


//   const slide_visible_about = document.querySelectorAll('.swiper-slide_about');

//   const activeElSlide = Array.prototype.find.call (slide_visible_about, item => item.classList.contains('swiper-slide-active'));

//   const idActiveSlide = activeElSlide.getAttribute('data-id');

//   const slide_visible_text = document.querySelectorAll('.slide__text__id');

//   const slide_visible_button = document.querySelectorAll('.slide__button__id');


//   slide_visible_text.forEach((element) => {
//     const slideVisibleTextEl = element.getAttribute('data-id');
//     if (idActiveSlide === slideVisibleTextEl) {
//       element.classList.add('text__active');
//     } else {
//       element.classList.remove('text__active');
//     }
//   });

//   slide_visible_button.forEach((element) => {
//     const slideVisibleButtonEl = element.getAttribute('data-id');
//     if (idActiveSlide === slideVisibleButtonEl) {
//       element.classList.add('text__active');
//     } else {
//       element.classList.remove('text__active');
//     }
//   });
// });

// let activeText = document.querySelector('.text__active')

// resize_paragraph_swiper(activeText)



const swiperNext = document.querySelector('.swiper-button-next-svg')
const swiperPrev = document.querySelector('.swiper-button-prev-svg')

// init height of paragraph container
gsap.to(swiperNext, {
  scrollTrigger: {
    trigger: swiperNext,
    scroller: "body",
    start: "top bottom",
    end: "top bottom",
    onEnter: () => resize_paragraph_swiper(), 
  }
});


swiperNext.addEventListener('click', ()=>{
  let textActive = document.querySelector('.text__active')
  if (textActive.nextElementSibling !== null){
    removeActive()
    textActive.nextElementSibling.classList.add('text__active')
    resize_paragraph_swiper()
  } else {
    removeActive()
    document.querySelector('.js__1__text[data-id="1"]').classList.add('text__active')
    resize_paragraph_swiper()
  }
})

swiperPrev.addEventListener('click', ()=>{
  let textActive = document.querySelector('.text__active')
  if (textActive.previousElementSibling !== null){
    removeActive()
    textActive.previousElementSibling.classList.add('text__active')
    resize_paragraph_swiper()
  } else {
    removeActive()
    document.querySelector('.js__3__text[data-id="3"]').classList.add('text__active')
    resize_paragraph_swiper()
  }
})


function removeActive(){
  let textActive = document.querySelector('.text__active')
  textActive.classList.remove('text__active')
}


function resize_paragraph_swiper(){
  let textActive = document.querySelector('.text__active')
  const about_text_parapgraph_swiper = document.querySelector('.about__slider__text__paragraph')
  about_text_parapgraph_swiper.style.height = `${textActive.clientHeight}px`
  // console.log(textActive.clientHeight)
}

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



