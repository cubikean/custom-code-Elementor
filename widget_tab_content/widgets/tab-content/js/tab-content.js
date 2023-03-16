"use strict";

function start(){

const bkTab = document.querySelector(".bk-tab__nav");
let rect = document.querySelector(".bk-tab__nav__bar");
const containerTop = document.querySelector('.bk-tab__container__top')
const containerIcon = document.querySelector('.bk-tab__container__icon')

if (rect) {

  const posItem = document.querySelectorAll(".posItem");
  const topSingle = document.querySelectorAll(".bk-tab__container__top__single");
  const topSingleImage = document.querySelectorAll(".bk-tab__container__top__single__image");
  const topSingleContent = document.querySelectorAll(".bk-tab__container__top__single__content");
  const topSingleContentImage = document.querySelectorAll(".bk-tab__container__top__single__content__image");
  const topSingleContentTitle = document.querySelectorAll(".bk-tab__container__top__single__content__title");
  const topSingleContentText = document.querySelectorAll(".bk-tab__container__top__single__content__text");
  const iconSingle = document.querySelectorAll(".bk-tab__container__icon__single");
  const iconSingleContent = document.querySelectorAll(".bk-tab__container__icon__single__content");
  const select = document.querySelector(".bk-tab__nav__select");

  function posElementLeft(e, v) {
    for (let i = v; i < e.length; i++) {
      let value =
        e[i].getBoundingClientRect().left - bkTab.getBoundingClientRect().left;
      return value;
    }
  }

  function posElementWidth(e, v) {
    for (let i = v; i < e.length; i++) {
      let valueW = e[i].getBoundingClientRect().width;
      return valueW;
    }
  }

  function resetActive() {
    posItem.forEach((item) => {
      item.classList.remove("bk-tab__nav__item--active");
    });
  }

  rect.style.width = posElementWidth(posItem, 0) + "px";
  rect.style.left = posElementLeft(posItem, 0) + "px";


  for (let i = 0; i < posItem.length; i++) {
      if(!topSingle[0].classList.contains('active')){
        topSingle[0].classList.add("active");
        topSingleImage[0].classList.add("active");
        topSingleContentImage[0].classList.add("active");
        topSingleContentTitle[0].classList.add("active");
        topSingleContentText[0].classList.add("active");
        iconSingle[0].classList.add("active");
      }
        
      posItem[i].addEventListener("click", (e) => {
      rect.style.width = posElementWidth(posItem, i) + "px";
      rect.style.left = posElementLeft(posItem, i) + "px";

      resetActive();

      e.target.classList.add("bk-tab__nav__item--active");

      
      topSingle.forEach(item => {
        item.classList.remove('active')
      });
      topSingleImage.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentText.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentImage.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentTitle.forEach(item => {
        item.classList.remove('active')
      });
      if(topSingle[i].classList.contains('is-disabled')){
        topSingle[i].classList.remove("is-disabled");
        topSingle[i].classList.add("active");
        setTimeout(() => {
          topSingleImage[i].classList.add("active");
          
        }, 100);
        setTimeout(() => {
          
        topSingleContentText[i].classList.add("active");
        topSingleContentTitle[i].classList.add("active");
        topSingleContentImage[i].classList.add("active");
      }, 300);
      } else {
        topSingle[i].classList.add("active");
        setTimeout(() => {
        topSingleImage[i].classList.add("active");
          
        }, 100);
        setTimeout(() => {
          
          // topSingleContent[i].classList.add("active");
          topSingleContentText[i].classList.add("active");
          topSingleContentTitle[i].classList.add("active");
        topSingleContentImage[i].classList.add("active");
      }, 300);
      }

      iconSingle.forEach(item => {
        
        item.classList.remove('active')
      });
      if(iconSingle[i].classList.contains('is-disabled')){
        iconSingle[i].classList.remove("is-disabled");
        iconSingle[i].classList.add("active");
      } else {
        iconSingle[i].classList.add("active");
      }


    });
  }

  select.addEventListener("change", () => {
    const i = select.value - 1;
    resetActive();
    posItem[i].classList.add("bk-tab__nav__item--active");
    // disabledAll();
    topSingle.forEach(item => {
      item.classList.remove('active')
    });
    topSingleImage.forEach(item => {
      item.classList.remove('active')
    });
    topSingleContentText.forEach(item => {
      item.classList.remove('active')
    });
    topSingleContentImage.forEach(item => {
      item.classList.remove('active')
    });
    topSingleContentTitle.forEach(item => {
      item.classList.remove('active')
    });
    if(topSingle[i].classList.contains('is-disabled')){
      topSingle[i].classList.remove("is-disabled");
      topSingle[i].classList.add("active");
      setTimeout(() => {
        topSingleImage[i].classList.add("active");
      }, 100);
      setTimeout(() => {
      topSingleContentImage[i].classList.add("active");
      topSingleContentText[i].classList.add("active");
      topSingleContentTitle[i].classList.add("active");
    }, 300);
    } else {
      topSingle[i].classList.add("active");
      setTimeout(() => {
      topSingleImage[i].classList.add("active");
      }, 100);
      setTimeout(() => {
        // topSingleContent[i].classList.add("active");
        topSingleContentText[i].classList.add("active");
        topSingleContentTitle[i].classList.add("active");
        topSingleContentImage[i].classList.add("active");
      }, 300);
    }
    iconSingle.forEach(item => {
      item.classList.remove('active')
    });
    if(iconSingle[i].classList.contains('is-disabled')){
      iconSingle[i].classList.remove("is-disabled");
      iconSingle[i].classList.add("active");
    } else {
      iconSingle[i].classList.add("active");
    }

  });
}
}

start();


function start2(){

  const bkTab = document.querySelector(".bk-tab__nav");
  const containerTop = document.querySelector('.bk-tab__container__top')
  const containerIcon = document.querySelector('.bk-tab__container__icon')
  
  
    const posItem = document.querySelectorAll(".posItem");
    const topSingle = document.querySelectorAll(".bk-tab__container__top__single");
    const topSingleImage = document.querySelectorAll(".bk-tab__container__top__single__image");
    const topSingleContent = document.querySelectorAll(".bk-tab__container__top__single__content");
    const topSingleContentImage = document.querySelectorAll(".bk-tab__container__top__single__content__image");
    const topSingleContentTitle = document.querySelectorAll(".bk-tab__container__top__single__content__title");
    const topSingleContentText = document.querySelectorAll(".bk-tab__container__top__single__content__text");
    const iconSingle = document.querySelectorAll(".bk-tab__container__icon__single");
    const iconSingleContent = document.querySelectorAll(".bk-tab__container__icon__single__content");
    const select = document.querySelector(".bk-tab__nav__select");
  
  
    for (let i = 0; i < posItem.length; i++) {
       
        posItem[i].addEventListener("click", (e) => {
  
        e.target.classList.add("bk-tab__nav__item--active");
        
        topSingle.forEach(item => {
          item.classList.remove('active')
        });
        topSingleImage.forEach(item => {
          item.classList.remove('active')
        });
        topSingleContentText.forEach(item => {
          item.classList.remove('active')
        });
        topSingleContentImage.forEach(item => {
          item.classList.remove('active')
        });
        topSingleContentTitle.forEach(item => {
          item.classList.remove('active')
        });
        if(topSingle[i].classList.contains('is-disabled')){
          topSingle[i].classList.remove("is-disabled");
          topSingle[i].classList.add("active");
          setTimeout(() => {
            topSingleImage[i].classList.add("active");
          }, 100);
          setTimeout(() => {
          topSingleContentText[i].classList.add("active");
          topSingleContentTitle[i].classList.add("active");
          topSingleContentImage[i].classList.add("active");
        }, 300);
        } else {
          topSingle[i].classList.add("active");
          setTimeout(() => {
          topSingleImage[i].classList.add("active");
          }, 100);
          setTimeout(() => {
            topSingleContentText[i].classList.add("active");
            topSingleContentTitle[i].classList.add("active");
          topSingleContentImage[i].classList.add("active");
        }, 300);
        }
  
        iconSingle.forEach(item => {
          
          item.classList.remove('active')
        });
        if(iconSingle[i].classList.contains('is-disabled')){
          iconSingle[i].classList.remove("is-disabled");
          iconSingle[i].classList.add("active");
        } else {
          iconSingle[i].classList.add("active");
        }
  
  
      });
    }
  // }
  
    select.addEventListener("change", () => {
      const i = select.value - 1;
      resetActive();
      posItem[i].classList.add("bk-tab__nav__item--active");
      topSingle.forEach(item => {
        item.classList.remove('active')
      });
      topSingleImage.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentText.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentImage.forEach(item => {
        item.classList.remove('active')
      });
      topSingleContentTitle.forEach(item => {
        item.classList.remove('active')
      });
      if(topSingle[i].classList.contains('is-disabled')){
        topSingle[i].classList.remove("is-disabled");
        topSingle[i].classList.add("active");
        setTimeout(() => {
          topSingleImage[i].classList.add("active");
        }, 100);
        setTimeout(() => {
        topSingleContentImage[i].classList.add("active");
        topSingleContentText[i].classList.add("active");
        topSingleContentTitle[i].classList.add("active");
      }, 300);
      } else {
        topSingle[i].classList.add("active");
        setTimeout(() => {
        topSingleImage[i].classList.add("active");
        }, 100);
        setTimeout(() => {
          // topSingleContent[i].classList.add("active");
          topSingleContentText[i].classList.add("active");
          topSingleContentTitle[i].classList.add("active");
          topSingleContentImage[i].classList.add("active");
        }, 300);
      }
      iconSingle.forEach(item => {
        item.classList.remove('active')
      });
      if(iconSingle[i].classList.contains('is-disabled')){
        iconSingle[i].classList.remove("is-disabled");
        iconSingle[i].classList.add("active");
      } else {
        iconSingle[i].classList.add("active");
      }
  
    });
  }


document.addEventListener('mousedown', (e)=>{
  if (e.target === document.querySelector('.elementor-editor-active .bk-tab__nav__item')){
    start();
  } else{
    start2();
  }
} )



