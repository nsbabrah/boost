(function($){

$.extend(jQuery.easing,{myfunc:function(x,t,b,c,d) { return x*x; }})

$.fn.slider = function(options){
  var options = $.extend({
    autoMove:              false,
    autoMoveOptions: {
      interval:            5000,
      pauseOnHover:        true,
    },
    buttonsEnabled:        true,
    buttonsOptions: {
      leftText:            "<",
      rightText:           ">",
    },
    bulletsEnabled:        true,
    slideWithFinger:       true,
    slideWithCursor:       true,
  }, options)

  return this.each(function(){
    var $c = $(this);

    $c.addClass("slider").append( $("<div></div>").addClass("slider-container").append( $c.find("*") ) );

    var $t = $c.children(".slider-container").first();

    $t.css({"width": $t.children("div").length*100+"%"});
    $t.children("div").css({"width": (1/$t.children("div").length)*100+"%"});
    $c.append( $("<div></div>").addClass("slider-navigation") );

    if ( options.buttonsEnabled ) {
      var $lB = $("<a></a>").attr("href", "#").addClass("slider-button-left").html( $("<span></span>").html( options.buttonsOptions.leftText ) );
      var $rB = $("<a></a>").attr("href", "#").addClass("slider-button-right").html( $("<span></span>").html( options.buttonsOptions.rightText ) );
      $c.find(".slider-navigation").append( $lB ).append( $rB );
    }

    if ( options.bulletsEnabled ) {
      var $buls = $("<ul></ul>").addClass("slider-bullets");
      $t.children("div").each(function(){
        $buls.append( $("<li></li>") );
        $(this).data("index", $(this).index());
      });
      $buls.children("li").first().addClass("current");
      $c.find(".slider-navigation").append( $buls );

      $buls.children("li").bind("click", function(){
        bulletsMove( $(this) );
      })
    }


    $t.children("div").last().prependTo( $t );

    var oMouseDown = oMouseMove = oMouseUp = "";

    if( options.slideWithFinger ){
      oMouseDown += "touchstart";
      oMouseMove += "touchmove";
      oMouseUp += "touchend";
    }

    if( options.slideWithCursor ){
      oMouseDown += " mousedown";
      oMouseMove += " mousemove";
      oMouseUp += " mouseup";
      $t.addClass("slider-cursor")
    }

    $lB.bind("click", function(e){
      e.preventDefault();
      moveToLeft();
    });

    $rB.bind("click", function(e){
      e.preventDefault();
      moveToRight();
    });

    $c.bind(oMouseDown, function(e){
      touchStart(e);
    });

    if( options.autoMove ){
      var timer = new RecurringTimer(function() {
        moveToRight();
      }, options.autoMoveOptions.interval+500);

      if( options.autoMoveOptions.pauseOnHover ){
        $c.bind("mouseover", function(){
          timer.pause();
        });

        $c.bind("mouseout", function(){
          timer.resume();
        });
      }
    }

    function moveToLeft(f){
      var win = $(window).width();
      var ease = (typeof(f)=="function") ? "linear": "swing";
      var time = (typeof(f)=="function") ? 200 : 500;
      $("ul li").removeClass("current").eq( $t.children("div").eq(0).data("index") ).addClass("current");
      $t.animate({"left": "0%"}, time, ease, function(){
        $t.prepend( $t.children("div").last() ).css("left", "-100%" );
        if(f == 1){
         $c.bind(oMouseDown, function(e){
           touchStart(e);
         });
        } else if( typeof(f) == "function" ){
          f();
        }
      });
    }

    function moveToRight(f){
      var win = $(window).width();
      var ease = (typeof(f)=="function") ? "linear": "swing";
      var time = (typeof(f)=="function") ? 200: 500;
      $("ul li").removeClass("current").eq( $t.children("div").eq(2).data("index") ).addClass("current");
      $t.animate({"left": "-200%"}, time, ease, function(){
        $t.append( $t.children("div").first() ).css("left", "-100%" );
          if(f == 1){
           $c.bind(oMouseDown, function(e){
             touchStart(e);
           });
          } else if( typeof(f) == "function" ){
            f();
          }
      });
    }

    function bulletsMove( $this ){
      var index = $this.index()
      var cardIndex = $t.children("div").eq(1).data("index")

      if( index > cardIndex ){
        moveToRight( function(){bulletsMove($this)} );
      } else if( index < cardIndex ){
        moveToLeft( function(){bulletsMove($this)} );
      }
    }

    function touchStart(e){
      e.preventDefault();
      var orgX = (typeof(e.originalEvent.touches) != "undefined") ? e.originalEvent.touches[0].pageX : e.pageX;
      var xStart = $t.css("left").replace("px", "")*1;
      var dX = 0;
      $c.bind(oMouseMove, function(e){
        e.preventDefault();
        var touch = (typeof(e.originalEvent.touches) != "undefined") ? e.originalEvent.touches[0].pageX : e.pageX;
        dX = touch - orgX;
        $t.css("left", (xStart+dX) );
      });

      $c.bind(oMouseUp, function(e){
        e.preventDefault();
        $(this).unbind(oMouseDown+" "+oMouseMove+" "+oMouseUp)
        .bind(oMouseDown, function(e){
          e.preventDefault();
        });

        if(dX>20){
          moveToLeft(1);
        } else if(dX<-20){
          moveToRight(1);
        } else {
          $t.animate({"left": "-100%"}, 100, function(){
            $c.bind(oMouseDown, function(e){
              touchStart(e);
            });
          });
        }
      });
    }

    function RecurringTimer(callback, delay) {
        var timerId, start, remaining = delay;

        this.pause = function() {
            window.clearTimeout(timerId);
            remaining -= new Date() - start;
        };

        var resume = function() {
            start = new Date();
            timerId = window.setTimeout(function() {
                remaining = delay;
                resume();
                callback();
            }, remaining);
        };

        this.resume = resume;

        this.resume();
    }

  })
}

})(jQuery)
