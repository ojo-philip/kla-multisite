$(document).ready(function () {
  $('.gallery-item').magnificPopup({
    delegate: 'a', // child items selector, by clicking on it popup will open
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      // options for gallery
      enabled: true,
      navigateByImageClick: true,
      preload: [0, 1]
    },
    image:{
      tError: '<a href= "%url%">The image #%curr%</a> could not be loaded',
      // titleSrc: function(item){
      //   return item.el.attr('title') + '<small>by Heritage Web Dev'
      // }
    }
    // other options
  });

});
