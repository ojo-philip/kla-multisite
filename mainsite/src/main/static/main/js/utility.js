$(document).ready(function () {
  $(".post-center-container").owlCarousel({
    loop: false,
    autoplay: true,
    // autoplayTimeout: 3000, 
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  })
  // owl carousel for events
  $(".events-center").owlCarousel({
    loop: false,
    // autoplay: true,
    autoplayTimeout: 3000,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 3
      }
    }
  })

  // owl carousel for gallery
  $(".gallery-container").owlCarousel({
    loop: false,
    autoplay: true,
    autoplayTimeout: 3000,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 2
      },
      1000: {
        items: 4
      }
    }
  })

})