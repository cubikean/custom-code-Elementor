
var $ = jQuery;
function video_zoom_script() {

      const video = document.querySelector("video");
      const absolText = document.querySelector(".absolText");
      const backVideo = document.querySelector(".bottomVideoBlur");
      const containervideo = document.querySelectorAll(".container-video");
      let tl = gsap.timeline({
        scrollTrigger: {
          trigger: video,
          start: "top 30%",
          end: "top top",
          markers: true,
          scrub: 2,
        //   pin:true,
        },
      });
      tl.from(video, {position:'relative', width: "65%", duration: 0.3 });
    //   tl.from(absolText, { opacity: 0, duration: 0.2 });
      tl.from(backVideo, {opacity: 0, duration: 0.3 });

      gsap.to(absolText, {
        scrollTrigger: {
          trigger: absolText,
          start: "top 20%",
          markers: true,
          toggleActions: "play none none reverse",
          // pin: ".box1",
          pinSpacing: false,
        },
        y:-15,
        opacity: 1,
        duration: 1,
      });

}

$(function() { bricksIsFrontend && video_zoom_script(); })

      