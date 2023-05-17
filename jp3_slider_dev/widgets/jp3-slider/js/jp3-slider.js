
     svgcircle1 = document.getElementById('circle1');

pathscircle1 = svgcircle1.getElementsByTagName("path");

svgcircle2 = document.getElementById('circle2');

pathscircle2 = svgcircle2.getElementsByTagName("path");

svgcircle3 = document.getElementById('circle3');

pathscircle3 = svgcircle3.getElementsByTagName("path");

const about_text = document.querySelectorAll(".about__container__right__text");
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
    markers:true,
  }
});

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

gsap.to(first_text, {
  scrollTrigger: {
    trigger: ".circle__1",
    scroller: "body",
    start: "top 120%",
    end: "top -10%",
    onEnter: () => add__first__text(),
    onLeave: () => remove__first__text(),
    onEnterBack: () => add__first__text(),
    onLeaveBack: () => remove__first__text(),
  }
});

gsap.to(second_text, {
  scrollTrigger: {
    trigger: ".circle__2",
    scroller: "body",
    start: "top 85%",
    end: "top -10%",
    onEnter: () => add__second__text(),
    onLeave: () => remove__second__text(),
    onEnterBack: () => add__second__text(),
    onLeaveBack: () => remove__second__text(),
  }
});

gsap.to(third_text, {
  scrollTrigger: {
    trigger: ".circle__3",
    scroller: "body",
    start: "top 85%",
    end: "top -55%",
    onEnter: () => add__third__text(),
    onLeave: () => remove__third__text(),
    onEnterBack: () => add__third__text(),
    onLeaveBack: () => remove__third__text(),
  }
});

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

      