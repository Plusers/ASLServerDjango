/*

Template:  
Author: potenzaglobalsolutions.com
Version:  
Design and Developed by: potenzaglobalsolutions.com

NOTE:  

*/
 
//Global var
var POTENZA = {};
 
 (function($){
  "use strict";



     //----------------------------------------------------/
    // Predefined Variables
    //----------------------------------------------------/
    var $window = $(window),
        $document = $(document),
        $body = $('body'),
        $countdownTimer = $('.countdown'),
        $progressBar = $('.progress-bar'),
        $counter = $('.counter');


   //Check if function exists
    $.fn.exists = function () {
        return this.length > 0;
    };

  /*************************
       preloader
  *************************/  
  POTENZA.preloader = function () {
       $("#load").fadeOut();
       $('#loading').delay(0).fadeOut('slow');
   };


/*************************
       mega menu
*************************/    
 POTENZA.megaMenu = function () {
    $('#menu').megaMenu({
           // DESKTOP MODE SETTINGS
          logo_align          : 'left',         // align the logo left or right. options (left) or (right)
          links_align         : 'left',        // align the links left or right. options (left) or (right)
          socialBar_align     : 'left',    // align the socialBar left or right. options (left) or (right)
          searchBar_align     : 'right',   // align the search bar left or right. options (left) or (right)
          trigger             : 'hover',           // show drop down using click or hover. options (hover) or (click)
          effect              : 'fade',             // drop down effects. options (fade), (scale), (expand-top), (expand-bottom), (expand-left), (expand-right)
          effect_speed        : 400,          // drop down show speed in milliseconds
          sibling             : true,              // hide the others showing drop downs if this option true. this option works on if the trigger option is "click". options (true) or (false)
          outside_click_close : true,  // hide the showing drop downs when user click outside the menu. this option works if the trigger option is "click". options (true) or (false)
          top_fixed           : false,           // fixed the menu top of the screen. options (true) or (false)
          sticky_header       : false,       // menu fixed on top when scroll down down. options (true) or (false)
          sticky_header_height: 250,  // sticky header height top of the screen. activate sticky header when meet the height. option change the height in px value.
          menu_position       : 'horizontal',    // change the menu position. options (horizontal), (vertical-left) or (vertical-right)
          full_width          : false,           // make menu full width. options (true) or (false)
         // MOBILE MODE SETTINGS
          mobile_settings     : {
            collapse            : true,    // collapse the menu on click. options (true) or (false)
            sibling             : true,      // hide the others showing drop downs when click on current drop down. options (true) or (false)
            scrollBar           : true,    // enable the scroll bar. options (true) or (false)
            scrollBar_height    : 400,  // scroll bar height in px value. this option works if the scrollBar option true.
            top_fixed           : false,       // fixed menu top of the screen. options (true) or (false)
            sticky_header       : false,   // menu fixed on top when scroll down down. options (true) or (false)
            sticky_header_height: 200   // sticky header height top of the screen. activate sticky header when meet the height. option change the height in px value.
         }
       });

}


 
/*************************
       owl-carousel 
*************************/

 POTENZA.carousel = function () {

    $(".owl-carousel").each(function () {
        var $this = $(this),
            $items = ($this.data('items')) ? $this.data('items') : 1,
            $loop = ($this.data('loop')) ? $this.data('loop') : true,
            $navdots = ($this.data('nav-dots')) ? $this.data('nav-dots') : false,
            $navarrow = ($this.data('nav-arrow')) ? $this.data('nav-arrow') : false,
            $autoplay = ($this.attr('data-autoplay')) ? $this.data('autoplay') : true,
            $space = ($this.attr('data-space')) ? $this.data('space') : 30;     
            $(this).owlCarousel({
                loop: $loop,
                items: $items,
                responsive: {
                  0:{items: $this.data('xxs-items') ? $this.data('xx-items') : 1},
                  500:{items: $this.data('xs-items') ? $this.data('xs-items') : 1},
                  767:{items: $this.data('sm-items') ? $this.data('sm-items') : 2},
                  992:{items: $this.data('md-items') ? $this.data('md-items') : 2},
                  1190:{items: $this.data('lg-items') ? $this.data('lg-items') : 3},
                  1200:{items: $items}
                },
                dots: $navdots,
                margin:$space,
                nav: $navarrow,
                navText:["<i class='fa fa-angle-left fa-2x'></i>","<i class='fa fa-angle-right fa-2x'></i>"],
                autoplay: $autoplay,
                autoplayHoverPause: true   
            }); 
           
    }); 
}


/*************************
          sidemenu
*************************/

 POTENZA.sidemenu = function () {
        var $menu_btn = $('.mobile-nav-button'),
            $overlay =  $('.menu-overlay'),
            $menucls =  $('.menu-close'),
            $slidemenu =  $('.side-content');


        $menu_btn.on('click', function () {
           if ($(".search").exists()){
             if ($(".search").hasClass('is-visible')){
                   return false;  
             }
           }


            toggleslidemenu();   
            return false;   
        });
       
        $overlay.on('click', function () {
            toggleslidemenu('close');
            return false;
        });
        $menucls.on('click', function () {
            toggleslidemenu('close');
            return false;
        });
        function toggleslidemenu(type) {
            if(type=="close") {
                $slidemenu.removeClass('side-content-open');
                $overlay.removeClass('is-visible');
              } else {         
                $slidemenu.addClass('side-content-open');
                $overlay.addClass('is-visible');
                
            }
         }
 }


/*************************
      Scroll to Top
*************************/
  POTENZA.scrolltotop = function () {  
      var $scrolltop = $('.back-to-top');

      $scrolltop.on('click', function () {
          $('html,body').animate({
                    scrollTop: 0
             }, 800);
          $(this).addClass("back-run");
          setTimeout(function(){ $scrolltop.removeClass('back-run');},1000);
          return false;
      });
      $window.on('scroll', function () {   
          if($window.scrollTop() >= 200) {
              $scrolltop.addClass("show");
              $scrolltop.addClass("back-down");
             } else {
               $scrolltop.removeClass("show");
               setTimeout(function(){ $scrolltop.removeClass('back-down');},300);
            }
       });
  }


/****************************************************
     POTENZA Window load and functions
****************************************************/

  //Window load functions
    $window.load(function () {
      POTENZA.preloader();
    });


  //Document ready functions
    $document.ready(function () {
        POTENZA.megaMenu(),
        POTENZA.carousel(),
        POTENZA.sidemenu(),
        POTENZA.scrolltotop();

    });


})(jQuery);