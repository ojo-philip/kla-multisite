const navBtn = document.querySelector(".nav-btn");
const navLinks = document.querySelector(".nav-links");
const navContent = document.querySelector(".nav-contents");
// const navDisplay = document.querySelector(".nav-display")


navBtn.addEventListener("click", function(){
  let linkContainerHeight = navContent.getBoundingClientRect().height;
  let navBarItemHeight = navLinks.getBoundingClientRect().height;
  if (linkContainerHeight == 0) {
    navContent.style.height = `${navBarItemHeight}px`;
  } else {
    navContent.style.height = 0
  }
  // navLinks.classList.toggle("show-links")
});
let footerYear = document.querySelector('.footer-date');
let year = new Date().getFullYear();
footerYear.textContent = year;

// accordion
const missions = document.querySelectorAll(".mission");

missions.forEach(function (mission) {
  const btn = mission.querySelector(".mission-btn");
  // console.log(btn);

  btn.addEventListener("click", function () {
    // console.log(question);

    missions.forEach(function (item) {
      if (item !== mission) {
        item.classList.remove("show-text");
      }
    });

    mission.classList.toggle("show-text");
  });
});

// tabs
const about = document.querySelector(".about");
const btns = document.querySelectorAll(".tab-btn");
const articles = document.querySelectorAll(".content");
about.addEventListener("click", function (e) {
  const id = e.target.dataset.id;
  if (id) {
    // remove selected from other buttons
    btns.forEach(function (btn) {
      btn.classList.remove("active");
    });
    e.target.classList.add("active");
    // hide other articles
    articles.forEach(function (article) {
      article.classList.remove("active");
    });
    const element = document.getElementById(id);
    element.classList.add("active");
  }
});
