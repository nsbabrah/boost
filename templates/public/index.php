

<html lang="en" >
	<head>
		<title >Boostlikes</title>
		<meta charset="utf-8" />
		<meta property="og:title" content=""/>
		<meta property="og:image" content=""/>
		<meta property="og:url" content=""/>
		<meta property="og:site_name" content=""/>
		<meta property="og:description" content=""/>
		<meta name="twitter:title" content="" />
		<meta name="twitter:image" content="" />
		<meta name="twitter:url" content="" />
		<meta name="twitter:card" content="" />
		<link rel="big-icon"style='background-size: 300px 150px;' background-image="../../static/images/rr.png" width="50%" height="50%" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="../../static/css/main.css" />
    <style type="text/css">
.main {
    background-image: url('../../static/images/rocket.png');
        background-size: cover;
}
.pg-canvas{

  height: 400px;
  width:400px;
}.wow {
   visibility: hidden;
}
#container{
background: #1c3149;
background: -moz-radial-gradient(center, ellipse cover,  #1c3149 0%, #0d121c 80%);
background: -webkit-gradient(radial, center center, 0px, center center, 100%, color-stop(0%,#1c3149), color-stop(80%,#0d121c));
background: -webkit-radial-gradient(center, ellipse cover,  #1c3149 0%,#0d121c 80%);
background: -o-radial-gradient(center, ellipse cover,  #1c3149 0%,#0d121c 80%);
background: -ms-radial-gradient(center, ellipse cover,  #1c3149 0%,#0d121c 80%);
background: radial-gradient(ellipse at center,  #1c3149 0%,#0d121c 80%);
overflow: hidden;
height: 100%;
margin:0;

}
#h1{
  background-image: url('../static/images/rocket.png');
      background-size: cover;
  position: absolute;

}#header {
    background-color: black;
    /*Opacity start*/
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    filter: alpha(opacity=80);
    -moz-opacity: 0.80;
    -khtml-opacity: 0.8;
    opacity: 0.8;
    /*Opacity end*/
    color: white;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 150px;
    padding: 0;
    margin: 0;
}
#header #header-content {
    margin: 10px;
}
</style>
<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,400italic|Josefin+Slab:400,700italic' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="../../static/css/normalize.css" type="text/css">
<link rel="stylesheet" href="../../static/css/animate.css" type="text/css">
<link rel="stylesheet" href="../../static/css/style.css" type="text/css">
<link rel="stylesheet" href="../../static/css/examples.css" type="text/css">
<link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
<link rel="stylesheet" href="../static/css/animate.css">

<link rel="stylesheet" href="../../static/model_pop_css/reset.css"> <!-- CSS reset -->
<link rel="stylesheet" href="../../static/model_pop_css/style.css"> <!-- Gem style -->
<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
<link rel="shortcut icon" href="favicon.ico">

<!-- Google Webfonts -->
<link href='http://fonts.googleapis.com/css?family=Roboto:400,300,100,500' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>

<!-- Animate.css -->
<link rel="stylesheet" href="../../static/css/css/animate.css">
<!-- Icomoon Icon Fonts-->
<link rel="stylesheet" href="../../static/css/css/icomoon.css">
<!-- Owl Carousel -->
<link rel="stylesheet" href="../../static/css/css/owl.carousel.min.css">
<link rel="stylesheet" href="../../static/css/css/owl.theme.default.min.css">
<!-- Magnific Popup -->
<link rel="stylesheet" href="../../static/css/css/magnific-popup.css">
<!-- Theme Style -->
<link rel="stylesheet" href="../../static/css/css/style.css">
<!-- Modernizr JS -->
<script src="../../static/js/js/modernizr-2.6.2.min.js"></script>
<!-- FOR IE9 below -->
<!--[if lt IE 9]>
<script src="js/respond.min.js"></script>
<![endif]-->

	<script src="../../static/js/jquery.min.js"></script>
      <script src="../../static/js/wow.js"></script>
<script src="../../static/js/control_wow.js"></script>
<!-- <script src="../../static/node_modules/angular/angular.min.js"></script><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>
	<script src="../../static/node_modules/angular-route/angular-route.js"></script>
<script src="../../static/node_modules/angular-route/angular-route.min.js"></script>
<script src="../../static/node_modules/angular-route/angular-route.min.js.map"></script>
<script src="../../static/node_modules/bootstrap/dist/js/bootstrap.min.js"></script> -->
<!--  //////////////////////////////////////////////////////////////////////////-->
<script src="../../static/js/angular.js"></script>
<style media="screen">
body {
background: ;
height: 100%;
width: 100%;
margin: 0;
padding: 0;
color:red;
}
h12 {
    /*display: block;*/
    font-size: 3em;
		/*color:pink;*/
    /*margin-top: 0.67em;
    margin-bottom: 0.67em;*/
    /*margin-left: 0;
    margin-right: 0;*/
    font-weight: bold;
}
p12{
	font-size: 2em;
	/*margin-top: 0.67em;
	margin-bottom: 0.67em;*/
	/*margin-left: 0;
	margin-right: 0;*/
	font-weight: bold;

}
</style>
<script>
var HeartsBackground = {
	// text:30px,
heartHeight: 60,
heartWidth: 64,
hearts: [],
heartImage: 'http://i58.tinypic.com/ntnw5.png',
maxHearts: 70,
minScale: 0.4,
draw: function() {

	this.setCanvasSize();
	this.ctx.clearRect(0, 0, this.w, this.h);
	this.ctx.font = "30px  non-seri";

	this.ctx.fillText("Boost Up your instagram growth potential!", 20, 320);
	this.ctx.font = "80px non-serif";
	this.ctx.fillText("BoostUplikes", 20, 280);

	this.ctx.fill()
	for (var i = 0; i < this.hearts.length; i++) {
		var heart = this.hearts[i];
		heart.image = new Image();
		heart.image.style.height = heart.height;
		heart.image.src = this.heartImage;
		this.ctx.globalAlpha = heart.opacity;
		this.ctx.drawImage (heart.image, heart.x, heart.y, heart.width, heart.height);
	}
	this.move();
},
move: function() {
	for(var b = 0; b < this.hearts.length; b++) {
		var heart = this.hearts[b];
		heart.y += heart.ys;
		if(heart.y > this.h) {
			heart.x = Math.random() * this.w;
			heart.y = -1 * this.heartHeight;
		}
	}
},
setCanvasSize: function() {
	this.canvas.width = window.innerWidth;
	this.canvas.height = window.innerHeight;
	this.w = this.canvas.width;
	this.h = this.canvas.height;
},
initialize: function() {
	this.canvas = $('#canvas')[0];

	if(!this.canvas.getContext)
		return;

	this.setCanvasSize();
	this.ctx = this.canvas.getContext('2d');

	this.ctx.font = "30px Arial";
	this.ctx.fillText("Hello World", 0, 220);
  this.ctx.fill()
// this.ctx== this.canvas.fillText("Hello World",10,50);
// this.ctx.strokeText("Hello World",10,50);
// 	// this.ctx= this.fill('asasasasa'50,10)

	for(var a = 0; a < this.maxHearts; a++) {
		var scale = (Math.random() * (1 - this.minScale)) + this.minScale;
		this.hearts.push({
			x: Math.random() * this.w,
			y: Math.random() * this.h,
			ys: Math.random() + 1,
			height: scale * this.heartHeight,
			width: scale * this.heartWidth,
			opacity: scale
		});
	}

	setInterval($.proxy(this.draw, this), 30);
}
};

$(document).ready(function(){
HeartsBackground.initialize();
	// HeartsBackground.ctx.fillText('2d');
});
</script>

	</head>
	<body  id="page-top" class="article">
<!--
		<div  id="main">
		      <div ng-view="app">


		          </div>
		</div> -->

								<!-- Mobile Toggle Menu Button -->


					<!-- END .header -->

				<!-- Banner -->



					<header id="fh5co-header"  >
						<!-- <header role="banner"> -->
							<!-- <div id="cd-logo"><a href="#0"><img src="img/cd-logo.svg" alt="Logo"></a></div> -->

							<nav class="main-nav">
								<ul>

<li><a class="cd-signin" name='main' href=""></a></li>
									<li><a class="cd-signup" href="signup#signup">Sign In</a></li>
								</ul>
							</nav>
						</header>
						<div >
						    <canvas width="800" id="canvas"height="800"></canvas>
								<h12 class="cd-signup" style="position:absolute;left:805px;top:220px;width:400px;">SIGN UP</h12>
								<p12 style="position:absolute;left:805px;top:245px;width:400px;">Today</p12>
						    <input type="text" placeholder="name"style="position:absolute;left:805px;top:300px;width:400px; etc...." />
								 <input type="text" placeholder="email"style="position:absolute;left:800px;top:350px;width:200px; etc...." />
								 <input type="text"placeholder="password" style="position:absolute;left:1010px;top:350px;width:200px; etc...." />
								 <button type="button" style="position:absolute;left:820px;top:400px;width:380px; etc...."class="btn btn-primary">Get Started</button>
						</div>

						<!-- <div id="canvas1"> -->


							<!-- <div class="fh5co-slider">
								<div class="owl-carousel owl-carousel-fullwidth">

								    <div class="item" style="background-image:url(../../css/static/images/slide_1.jpg)">
								    	<div class="fh5co-overlay"></div>
								    	<div class="container">
								    		<div class="row">
								    			<div class="col-md-8 col-md-offset-2">
									    			<div class="fh5co-owl-text-wrap">
												    	<div class="fh5co-owl-text text-center to-animate">
												    		<h1 class="fh5co-lead">Boostlikes</h1>
															<h2 class="fh5co-sub-lead">Let Boost Up Your Instagram profile <a href="#">Boostlikes</a></h2>
															<p ><h1  class="animated bounceInRight">Boostlikes.ca</h1>

															</div>
												    </div>
											    </div>
								    		</div>
								    	</div>
								    </div>
								    <div class="item" style="background-image:url(../../static/css/images/slide_2.jpg)">
								    	<div class="fh5co-overlay"></div>
								    	<div class="container">
								    		<div class="row">
								    			<div class="col-md-8 col-md-offset-2">
									    			<div class="fh5co-owl-text-wrap">
												    	<div class="fh5co-owl-text text-center to-animate">
												    		<h1 class="fh5co-lead">A Digital Studio</h1>
															<h2 class="fh5co-sub-lead"> You just need to sit back and relax <a href="#"></a>Boostlikes even manage your profile</h2>
												    	</div>
												    </div>
											    </div>
								    		</div>
								    	</div>
								    </div>
								    <div class="item" style="background-image:url(../../static/css/images/slide_3.jpg)">
								    	<div class="fh5co-overlay"></div>
								    	<div class="container">
								    		<div class="row">
								    			<div class="col-md-8 col-md-offset-2">
									    			<div class="fh5co-owl-text-wrap">
												    	<div class="fh5co-owl-text text-center to-animate">
												    		<h1 class="fh5co-lead">Branding, UX under in one roof</h1>
															<h2 class="fh5co-sub-lead">Providing best service for your growth<a href="#"></a></h2>
												    	</div>
												    </div>
											    </div>
								    		</div>
								    	</div>
								    </div>
								    <div class="item" style="background-image:url(../../static/css/images/slide_4.jpg)">
								    	<div class="fh5co-overlay"></div>
								    	<div class="container">
								    		<div class="row">
								    			<div class="col-md-8 col-md-offset-2">
									    			<div class="fh5co-owl-text-wrap">
												    	<div class="fh5co-owl-text text-center to-animate">
												    		<h1 class="fh5co-lead">Performence</h1>
															<h2 class="fh5co-sub-lead">Help your instagram profile to improve<a href="#"></a>100K likes and more</h2>
												    	</div>
												    </div>
											    </div>
								    		</div>
								    	</div>
								    </div>
								</div>
							</div>
 -->

				<!-- Main -->
					<!-- <div id="main" > -->

					<!-- Section -->
							<section class="wrapper style1">
								<div class="inner">
									<!-- 2 Columns -->
										<section class="wow fadeInUp" data-wow-delay="0s"  style="visibility: visible; animation-name: fadeInUp;">
										<div class="flex flex-2">
											<div class="col col1">
												<div class="image round fit">
													<a href="generic.html"><img src="../../static/images/boost1.png" alt="" /></a>
												</div>
											</div>


											<div class="col col2">
												<h3>Easy to Use</h3>
												<p>With our service, you just need to sit back and relax. <br>Well actually you just need to post pictures, and watch your account grow!</p>
												<a href="about" class="button">Learn More</a>
											</div>
										</div>
								</div>
							</section>
		</section>
						<!-- Section -->
							<section class="wrapper style2">
								<div class="inner">
									<section class="wow fadeInUp" data-wow-delay="0s" style="visibility: visible; animation-name: fadeInUp;">
									<div class="flex flex-2">
										<div class="col col2">
											<h3>Safe to Use</h3>
											<p>With our service your account is completely safe. The login credentials are stored in encryption</p>
											<a href="about" class="button">Learn More</a>
										</div>
										<div class="col col1 first">
											<div class="image round fit">
												<a href="" class="link"><img src="../static/images/boost_comment.png" alt="" /></a>
											</div>
										</div>
									</div>
								</div>
							</section>
						</section>
						<!-- Section -->

						<section class="wrapper style1">
							<div class="inner">
								<!-- 2 Columns -->
									<section class="wow fadeInUp" data-wow-delay="1s"  style="visibility: visible; animation-name: fadeInUp;">
									<div class="flex flex-2">
										<div class="col col1">
											<div class="image round fit">
												<a href="generic.html"><img src="../static/images/boost_100k.png" alt="" /></a>
											</div>
										</div>


										<div class="col col2">
											<h3>Powerful Feature</h3>
											<p>You get likes from real instagram users with real followers. You can even add extra packages to improve your account growth.</p>
											<a href="#" class="button">Learn More</a>
										</div>

										<div class="col col2">
											<h3>Grow Your Business Fast</h3>
											<p>With the likes that we provide, your picture will get a lot more impressions, more people will know about your awesome ideas and more people will follow you.</p>
									</div>
							</div>
						</section>


							<section class="wrapper style1" >
								<div class="inner">
									<header class="align-center">
										<h2>Invite your fiernds</h2>
										<p>Deals for suggesting</p>
									</header>
													<section class="wow slideInRight" data-wow-offset="10">
									<div class="flex flex-3">
										<div class="col align-center">
											<div class="image round fit">
												<img src="../static/images/rocket.png" alt="" />
											</div>

											<div class="col-sm-12 wow">
												<h3>Inviting 1</h3>
												<p>With our service, you just need to sit back and relax. <br>Well actually you just need to post pictures, and watch your account grow!</p>
												<!-- <a href="about" class="button">Learn More</a> -->
											</div>

										</div>

										<div class="col align-center">
											<div class="image round fit">
												<img src="../static/images/rocket2.png" alt="" />
											</div>

											<div class="col-sm-12 wow">
												<h3>Inviting 2</h3>
												<p>With our service, you just need to sit back and relax. <br>Well actually you just need to post pictures, and watch your account grow!</p>
												<!-- <a href="about" class="button">Learn More</a> -->
											</div>
											<!-- <a href="#" class="button">Learn More</a> -->
										</div>
										<div class="col align-center">
											<div class="image round fit">
												<img src="../static/images/rr.png" alt="" />
											</div>

											<div class="col-sm-12 wow">
												<h3>Inviting 3</h3>
												<p>With our service, you just need to sit back and relax. <br>Well actually you just need to post pictures, and watch your account grow!</p>
												<!-- <a href="about" class="button">Learn More</a> -->
											</div>
											<!-- <a href="about" class="button">Learn More</a> -->
										</div>
									</div>
								</div>
		            <!-- <section class="wow slideInLeft" data-wow-duration="2s" data-wow-delay="5s"></section>
		            <section class="wow slideInRight" data-wow-offset="10"  data-wow-iteration="10"></section> -->

							</section>
		</section>
					</div>


				<!-- Footer -->
					<footer id="footer">
						<div class="copyright">
							<ul class="icons">
								<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
								<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
								<li><a href="#" class="icon fa-instagram"><span class="label">Instagram</span></a></li>
								<li><a href="#" class="icon fa-snapchat"><span class="label">Snapchat</span></a></li>
							</ul>
							<p>&copy; Boostlikes<a href=""></a>.ca <a href=""></a></p>
						</div>
					</footer>

		<!-- Scripts -->
			<script src="../../static/js/jquery.min.js"></script>
        	<script src="../../static/js/wow.min.js"></script>
			<script src="../../static/js/jquery.scrolly.min.js"></script>
			<script src="../../static/js/jquery.scrollex.min.js"></script>
			<script src="../../static/js/skel.min.js"></script>
		<script src="../../static/js/util.js"></script>
				<script src="../../static/js/main.js"></script>
				<script src="../../static/js/js/jquery.min.js"></script>
				<!-- jQuery Easing -->
				<script src="../../static/js/js/jquery.easing.1.3.js"></script>
				<!-- Bootstrap -->
				<script src="../../static/js/js/bootstrap.min.js"></script>
				<!-- Owl carousel -->
				<script src="../../static/js/js/owl.carousel.min.js"></script>
				<!-- Waypoints -->
				<script src="../../static/js/js/jquery.waypoints.min.js"></script>
				<!-- Magnific Popup -->
				<script src="../../static/js/js/jquery.magnific-popup.min.js"></script>
				<!-- Main JS -->
				<script src="../../static/js/js/main.js"></script>
				<script src="../../static/model_pop_js/main.js"></script> <!-- Gem jQuery -->


      	<!-- <script src="../../static/js/ball_animation.js"></script>
        <!-- <script src="../../static/js/staranimate.js"></script> -->

	<!-- <script type="text/javascript" src="../../static/js/tracking.js"></script>
  <script type="text/javascript" src="../../static/js/lib/jquery.min.js"></script>
  <script type="text/javascript" src="../../static/js/lib/highlight.pack.js"></script>
  <script type="text/javascript" src="../../static/js/lib/modernizr.custom.min.js"></script>
  <script type="text/javascript" src="../../static/js/examples.js"></script>

  <script type="text/javascript" src="../../../js/lib/greensock/TweenMax.min.js"></script>
  <script type="text/javascript" src="../../static/scrollmagic/uncompressed/ScrollMagic.js"></script>
  <script type="text/javascript" src="../../static/scrollmagic/uncompressed/plugins/animation.gsap.js"></script>
  <script type="text/javascript" src="../../static/scrollmagic/uncompressed/plugins/debug.addIndicators.js"></script> -->
	</body>
</html
