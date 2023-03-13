const videos = document.querySelectorAll(".BK-video");
const absoluteTexts = document.querySelectorAll(".BK-absolText");
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
  tl.from(video, { position: "relative", width: "65%", height: "60vh", duration: 0.3 });
  tl.from(backVideos[index], { opacity: 0, duration: 0.3 });

  gsap.to(absoluteTexts[index], {
    scrollTrigger: {
      trigger: absoluteTexts[index],
      start: "top 45%",
      toggleActions: "play none none reverse",
      pinSpacing: false,
    },
    y: -15,
    opacity: 1,
    duration: 1,
  });
});

document.addEventListener('load', ()=>{
  absoluteTexts.forEach(element => {
    element.classList.remove('test')
  });
})
