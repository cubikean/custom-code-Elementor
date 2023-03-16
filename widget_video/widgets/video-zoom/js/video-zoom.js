const videos = document.querySelectorAll(".BK-video");
const absoluteTexts = document.querySelectorAll(".BK-absolText");
const numText = document.querySelectorAll(".decompte");
const absoluteSubTexts = document.querySelectorAll(".BK-absolSubText");
const backVideos = document.querySelectorAll(".BK-bottomVideoBlur");
const containerVideos = document.querySelectorAll(".BK-container-video");

videos.forEach((video, index) => {
  let tl = gsap.timeline({
    scrollTrigger: {
      trigger: video,
      start: "top 30%",
      end: "top top",
      scrub: 2,
    },
  });
  tl.from(video, { position: "relative", width: "60%", height: "60vh", borderRadius: '20px', duration: 0.3 });
  tl.from(backVideos[index], { opacity: 0, duration: 0.3 });

  gsap.to(absoluteTexts[index], {
    scrollTrigger: {
      trigger: absoluteTexts[index],
      start: "top 66%",
      toggleActions: "play none none reverse",
      pinSpacing: false,
    },
    y: -15,
    opacity: 1,
    duration: 1,
  });
  gsap.to(absoluteSubTexts[index], {
    scrollTrigger: {
      trigger: absoluteSubTexts[index],
      start: "top 70%",
      toggleActions: "play none none reverse",
      pinSpacing: false,
    },
    y: -15,
    opacity: 1,
    duration: 1,
  });

  gsap.set(
    numText[index],
    {
      textContent: 0,
      duration: 3,
      ease: Power1.easeIn,
      snap: { textContent: 1 },
      stagger: 1,
      
    }
  );
  gsap.to(
    numText[index],
    {
      textContent: numText[index].dataset.number,
      duration: 1,
      ease: Power1.easeIn,
      snap: { textContent: 1 },
      stagger: 1,
      
    }
  );
  gsap.to(
    numText[index],
    {
      textContent: numText[index].dataset.number,
      duration: 1,
      ease: Power1.easeIn,
      snap: { textContent: 1 },
      stagger: 1,
      scrollTrigger: {
        trigger: numText[index],
        start: "top 66%",
        // markers:true,
        toggleActions: "play none none reverse",
        pinSpacing: false,
      },
    }
  );
});

document.addEventListener('load', ()=>{
  absoluteTexts.forEach(element => {
    element.classList.remove('test')
  });
})
