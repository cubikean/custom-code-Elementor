const bkTab = document.querySelector(".bk-tab__nav");
let rect = document.querySelector(".bk-tab__nav__bar");
if (rect) {
  const posItem = document.querySelectorAll(".posItem");
  const topSingle = document.querySelectorAll(".bk-tab__container__top__single");
  const iconSingle = document.querySelectorAll(".bk-tab__container__icon__single");
  const select = document.querySelector('.bk-tab__nav__select')


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

  function disabledAll() {
    topSingle.forEach((item) => {
      item.classList.add("is-disabled");
    });
    iconSingle.forEach((item) => {
        item.classList.add("is-disabled");
      });
  }

  rect.style.width = posElementWidth(posItem, 0) + "px";
  rect.style.left = posElementLeft(posItem, 0) + "px";

  for (let i = 0; i < posItem.length; i++) {
    posItem[i].addEventListener("click", (e) => {
      rect.style.width = posElementWidth(posItem, i) + "px";
      rect.style.left = posElementLeft(posItem, i) + "px";
      resetActive();
      e.target.classList.add("bk-tab__nav__item--active");
      disabledAll();
      topSingle[i].classList.remove('is-disabled')
      iconSingle[i].classList.remove('is-disabled')
    });
  }
  select.addEventListener('change', ()=>{
    const i = select.value - 1;
    resetActive();
    posItem[i].classList.add("bk-tab__nav__item--active")
    disabledAll();
    topSingle[i].classList.remove('is-disabled')
    iconSingle[i].classList.remove('is-disabled')
})
}


