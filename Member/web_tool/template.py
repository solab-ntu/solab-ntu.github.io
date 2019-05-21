# -*- coding: utf-8 -*-

class Member():

	script1 = u"""
	<!doctype html>

	<!--[if lt IE 7]><html class="no-js ie6 oldie" lang="en"><![endif]-->
	<!--[if IE 7]><html class="no-js ie7 oldie" lang="en"><![endif]-->
	<!--[if IE 8]><html class="no-js ie8 oldie" lang="en"><![endif]-->
	<!--[if gt IE 8]><!-->
	<html class="no-js" lang="en">
	<!--<![endif]-->

	<!-- | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	Version: 1.3

	- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - | -->

	<head>

		<title>SOLab | 成員Member</title>

		<!-- Meta -->
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="robots" content="all" />
		<meta name="generator" content="RapidWeaver" />
		<link rel="icon" href="http://solab.me.ntu.edu.tw/favicon.ico" type="image/x-icon" />
		<link rel="shortcut icon" href="http://solab.me.ntu.edu.tw/favicon.ico" type="image/x-icon" />
		<link rel="apple-touch-icon" href="http://solab.me.ntu.edu.tw/apple-touch-icon.png" />


		<!-- CSS -->
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/styles.css" />
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/styles.min.css" />
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/colors-page1.css" />

		<!-- Conditional Stylesheets for Internet Explorer 7, 8 and 9 -->
		<!--[if IE 9]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie9.css" media="all"/><![endif]-->
		<!--[if IE 8]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie8.css" media="all"/><![endif]-->
		<!--[if IE 7]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie7.css" media="all"/><![endif]-->

		<!-- JavaScript : Include and embedded version -->
		<script src="../../rw_common/themes/stuffy/javascript.js"></script>
		<script src="../../rw_common/themes/stuffy/js/modernizr-respond.min.js"></script>
		<script src="../../rw_common/themes/stuffy/js/jquery.min.js"></script>
		<script src="../../rw_common/themes/stuffy/js/scripts.min.js"></script>
		<script>
			RwSet = {
				pathto: "../../rw_common/themes/stuffy/javascript.js",
				baseurl: "http://solab.me.ntu.edu.tw/"
			};
		</script>

		<!-- JavaScript & CSS : Style Variations -->
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/options/extracontent.js"></script>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/body/width/1000.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/body/bg/hide.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/fonts/body/helvetica.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/fonts/headings/trebuchet.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/title/font-size/30.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/slogan/font-size/22.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/logo/left.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/navigation/position/right.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/navigation/font-size/14.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/primary/font-size/14.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/secondary/position/right.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/secondary/font-size/13.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/footer/font-size/12.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/extra/font-size/16.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/banner/height/res.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/banner/slides/none.css" />
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/fade.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/horizontal.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/reverse-true.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/slide-6000.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/anim-600.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/easing/swing.js"></script>

		<style type="text/css" media="all">
			@import url(https://fonts.googleapis.com/earlyaccess/notosanstc.css);
		</style>

	</head>

	<body>
		<div id="wrap">
			<header>
				<div id="top">
					<div id="headings" class="clearfix">
						<div id="logo">
							<a href="http://solab.me.ntu.edu.tw/">
								<img src="../../rw_common/images/rwsitelogo.png" width="129" height="75" alt="Site logo" />
							</a>
						</div>
						<!-- logo -->
						<h1 id="title">
							<a href="http://solab.me.ntu.edu.tw/">
								<div style="font-family: 'Noto Sans TC', sans-serif; line-height:1.1em">國立台灣大學 系統最佳化實驗室
									<br>
								</div>
							</a>
							<span id="slogan">
								<div style="font-family: 'Noto Sans TC', sans-serif;">System Optimization Laboratory, National Taiwan University</div>
							</span>
							<!-- slogan -->
						</h1>
						<!-- title -->
						<div id="extraContainer1">
							<!--extra user content renders here-->
						</div>
						<!-- extra content -->
					</div>
				</div>
				<div id="wrap-nav">
					<nav id="navigation" class="clearfix">
						<ul class="menu">
							<li>
								<a href="../../index.html" rel="self">首頁 | Home</a>
							</li>
							<li>
								<a href="../../Research/Research.html" rel="self">研究 | Research</a>
								<ul class="menu">
									<li>
										<a href="../../Research/Research/Research_1.html" rel="self">設計+不確定因素
											<br>&nbsp Design+Uncertainty</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_2.html" rel="self">複雜系統+不確定因素
											<br>&nbsp Complex System+Uncertainty</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_3.html" rel="self">動態+規劃
											<br>&nbsp Dynamic+Planning</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_4.html" rel="self">智慧載具+可靠度
											<br>&nbsp Intelligent Vehicle+Reliability</a>
									</li>
								</ul>
							</li>
							<li class="current">
								<a href="../Member/Member.html" rel="self">成員 | Member</a>
								<ul class="menu">
									<li>
										<a href="../../Member/Member/Member.html" rel="self">現任成員 | Current Member</a>
									</li>
									<li>
										<a href="../../Member/Alumni/Alumni.html" rel="self">畢業學生 | Alumni</a>
									</li>
								</ul>
							</li>
							<li>
								<a href="../../Teaching/Teaching.html" rel="self">課程 | Teaching</a>
							</li>
							<li>
								<a href="../../ContactInfo/ContactInfo.html" rel="self">聯絡方式 | Contact info</a>
							</li>
						</ul>
					</nav>
				</div>
				<!-- nav -->
				<div id="header-container">
					<div id="banner">
						<div id="slides">
							<div id="extraContainer2">
								<!--extra user content renders here-->
							</div>
						</div>
						<!-- extra content -->
					</div>
					<!-- banner -->
				</div>
				<!-- header-container -->
			</header>
			<!-- header -->
			<div id="extraContainer3">
				<!--extra user content renders here-->
			</div>
			<div id="main-container">
				<div id="main" class="clearfix">
					<section id="primary-container">
						<span style="font:17px Verdana, serif; font-weight:bold; color:#000000;font-weight:bold; ">Current Member</span>
						<span style="font:17px Verdana, serif; font-weight:bold; font-weight:bold; ">
							<br />
							<br />
						</span>
						<code><table style="line-height:15px"><tr valign=bottom></tr><tr valign=bottom><td></code>
	"""

	script2 = u"""
						<span style="font:12px STHeitiTC-Light; ">
							<a href="{0}" rel="self" title="{1}">{2}</a>
						</span>
						<code><a href="{0}" rel="self" title="{1}"><br></a></code>
						<span style="font:12px Arial, Verdana, Helvetica, sans-serif; ">
							<a href="{0}" rel="self" title="{1}">{1}
								<br>
							</a>
						</span>
						<span style="font:12px Arial, Verdana, Helvetica, sans-serif; ">
							<a href="{0}" rel="self" title="{1}">
								<img class="imageStyle" alt="{1}" src="{3}" width="150" height="113" />
							</a>
						</span>
	"""

	script3_1 = u"""
						<code></td></tr><tr valign=bottom><td></code>
	"""

	script3_2 = u"""
						<code></td><td></code>
	"""

	script4 = u"""
						<code></td></tr></table></code>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;">For more info of each member, please click his/her picture. You can also find our previous members at </span>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;">
							<a href="../../Member/Alumni/Alumni.html" rel="self" title="Alumni">SOLab Alumni</a>
						</span>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;"> page.</span>
					</section>
					<!-- #primary-container -->
					<aside id="secondary-container">
						<h3></h3>
						<div id="sidebar">

						</div>
						<!-- #sidebar -->
						<div id="plugin-sidebar">

						</div>
						<!-- #plugin-sidebar -->
					</aside>
					<!-- #secondary-container -->
				</div>
				<!-- #main -->
			</div>
			<!-- #main-container -->
			<div id="bottom">
				<div id="breadcrumb"></div>
				<!-- #breadcrumb -->
				<div id="extraContainer4">
					<!--extra user content renders here-->
				</div>
			</div>
			<div id="footer-container">
				<footer>
					<p>&copy; 2015 Kuei-Yuan Chan
						<a href="#" id="rw_email_contact">Contact Me</a>
						<script type="text/javascript">var _rwObsfuscatedHref0 = "mai"; var _rwObsfuscatedHref1 = "lto"; var _rwObsfuscatedHref2 = ":ch"; var _rwObsfuscatedHref3 = "ank"; var _rwObsfuscatedHref4 = "y@n"; var _rwObsfuscatedHref5 = "tu."; var _rwObsfuscatedHref6 = "edu"; var _rwObsfuscatedHref7 = ".tw"; var _rwObsfuscatedHref = _rwObsfuscatedHref0 + _rwObsfuscatedHref1 + _rwObsfuscatedHref2 + _rwObsfuscatedHref3 + _rwObsfuscatedHref4 + _rwObsfuscatedHref5 + _rwObsfuscatedHref6 + _rwObsfuscatedHref7; document.getElementById('rw_email_contact').href = _rwObsfuscatedHref;</script>
					</p>
				</footer>
				<!-- footer -->
			</div>
			<!-- #footer-container -->
		</div>
		<!-- #wrap -->
	</body>

	</html>
	"""

class MemberPage():
	script1 = u"""
						<code></td></tr></table></code>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;">For more info of each member, please click his/her picture. You can also find our previous members at </span>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;">
							<a href="../../Member/Alumni/Alumni.html" rel="self" title="Alumni">SOLab Alumni</a>
						</span>
						<span style="font:13px Times, Georgia, Courier, serif; color:#000000;"> page.</span>
					</section>
					<!-- #primary-container -->
					<aside id="secondary-container">
						<h3></h3>
						<div id="sidebar">
	"""

	script2_1 = u"""
							<img class="imageStyle" src="{0}" width="300" height="225" />
							<br />
							<span style="font:16px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; ">{1} {2}</span>
							<br />
							<span style="font:16px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; ">{3}</span>
							<hr>
	"""

	script2_1_1 = u"""
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>學歷 Educations</u></span>
							<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">{0}</span>
							<code></p></code>
	"""

	script2_2 = u"""
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>研究領域 Research</u></span>
							<br />
							<code><p style="line-height:15px"></code>
							<span style="font:13px STHeitiTC-Light;">
								{0}
							</span>
							<code><p style="margin-top: 0.5em;line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
								{1}
							</span>
							<code></p></code>
	"""

	script3_1 = u"""
							<br />
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>期刊 / 會議論文 Papers</u></span>
							<br />
	"""

	script3_2 = u"""		<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
							{0}
							</span>
							<code></p></code>
	"""

	script3_3 = u"""		<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
							{0} <a href="{1}" rel="external">(Link)</a>
							</span>
							<code></p></code>
	"""

	script4 = u"""
						</div>
						<!-- #plugin-sidebar -->
					</aside>
					<!-- #secondary-container -->
				</div>
				<!-- #main -->
			</div>
			<!-- #main-container -->
			<div id="bottom">
				<div id="breadcrumb"></div>
				<!-- #breadcrumb -->
				<div id="extraContainer4">
					<!--extra user content renders here-->
				</div>
			</div>
			<div id="footer-container">
				<footer>
					<p>&copy; 2015 Kuei-Yuan Chan
						<a href="#" id="rw_email_contact">Contact Me</a>
						<script type="text/javascript">var _rwObsfuscatedHref0 = "mai"; var _rwObsfuscatedHref1 = "lto"; var _rwObsfuscatedHref2 = ":ch"; var _rwObsfuscatedHref3 = "ank"; var _rwObsfuscatedHref4 = "y@n"; var _rwObsfuscatedHref5 = "tu."; var _rwObsfuscatedHref6 = "edu"; var _rwObsfuscatedHref7 = ".tw"; var _rwObsfuscatedHref = _rwObsfuscatedHref0 + _rwObsfuscatedHref1 + _rwObsfuscatedHref2 + _rwObsfuscatedHref3 + _rwObsfuscatedHref4 + _rwObsfuscatedHref5 + _rwObsfuscatedHref6 + _rwObsfuscatedHref7; document.getElementById('rw_email_contact').href = _rwObsfuscatedHref;</script>
					</p>
				</footer>
				<!-- footer -->
			</div>
			<!-- #footer-container -->
		</div>
		<!-- #wrap -->
	</body>

	</html>
	"""

class Alumni():
	script1 = u"""
	<!doctype html>

	<!--[if lt IE 7]><html class="no-js ie6 oldie" lang="en"><![endif]-->
	<!--[if IE 7]><html class="no-js ie7 oldie" lang="en"><![endif]-->
	<!--[if IE 8]><html class="no-js ie8 oldie" lang="en"><![endif]-->
	<!--[if gt IE 8]><!-->
	<html class="no-js" lang="en">
	<!--<![endif]-->

	<!-- | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	Version: 1.3

	- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - | -->

	<head>

		<title>SOLab | 成員Member</title>

		<!-- Meta -->
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="robots" content="all" />
		<meta name="generator" content="RapidWeaver" />
		<link rel="icon" href="http://solab.me.ntu.edu.tw/favicon.ico" type="image/x-icon" />
		<link rel="shortcut icon" href="http://solab.me.ntu.edu.tw/favicon.ico" type="image/x-icon" />
		<link rel="apple-touch-icon" href="http://solab.me.ntu.edu.tw/apple-touch-icon.png" />


		<!-- CSS -->
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/styles.css" />
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/styles.min.css" />
		<link rel="stylesheet" href="../../rw_common/themes/stuffy/colors-page1.css" />

		<!-- Conditional Stylesheets for Internet Explorer 7, 8 and 9 -->
		<!--[if IE 9]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie9.css" media="all"/><![endif]-->
		<!--[if IE 8]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie8.css" media="all"/><![endif]-->
		<!--[if IE 7]><link rel="stylesheet" href="../../rw_common/themes/stuffy/css/ie/ie7.css" media="all"/><![endif]-->

		<!-- JavaScript : Include and embedded version -->
		<script src="../../rw_common/themes/stuffy/javascript.js"></script>
		<script src="../../rw_common/themes/stuffy/js/modernizr-respond.min.js"></script>
		<script src="../../rw_common/themes/stuffy/js/jquery.min.js"></script>
		<script src="../../rw_common/themes/stuffy/js/scripts.min.js"></script>
		<script>
			RwSet = {
				pathto: "../../rw_common/themes/stuffy/javascript.js",
				baseurl: "http://solab.me.ntu.edu.tw/"
			};
		</script>

		<!-- JavaScript & CSS : Style Variations -->
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/options/extracontent.js"></script>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/body/width/1000.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/body/bg/hide.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/fonts/body/helvetica.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/fonts/headings/trebuchet.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/title/font-size/30.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/slogan/font-size/22.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/header/logo/left.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/navigation/position/right.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/navigation/font-size/14.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/primary/font-size/14.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/secondary/position/right.css"
		/>
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/secondary/font-size/13.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/footer/font-size/12.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/extra/font-size/16.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/banner/height/res.css" />
		<link rel="stylesheet" type="text/css" media="screen" href="../../rw_common/themes/stuffy/css/banner/slides/none.css" />
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/fade.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/horizontal.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/reverse-true.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/slide-6000.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/anim-600.js"></script>
		<script type="text/javascript" src="../../rw_common/themes/stuffy/css/banner/slides/easing/swing.js"></script>

		<style type="text/css" media="all">
			@import url(https://fonts.googleapis.com/earlyaccess/notosanstc.css);
		</style>

	</head>

	<body>
		<div id="wrap">
			<header>
				<div id="top">
					<div id="headings" class="clearfix">
						<div id="logo">
							<a href="http://solab.me.ntu.edu.tw/">
								<img src="../../rw_common/images/rwsitelogo.png" width="129" height="75" alt="Site logo" />
							</a>
						</div>
						<!-- logo -->
						<h1 id="title">
							<a href="http://solab.me.ntu.edu.tw/">
								<div style="font-family: 'Noto Sans TC', sans-serif; line-height:1.1em">國立台灣大學 系統最佳化實驗室
									<br>
								</div>
							</a>
							<span id="slogan">
								<div style="font-family: 'Noto Sans TC', sans-serif;">System Optimization Laboratory, National Taiwan University</div>
							</span>
							<!-- slogan -->
						</h1>
						<!-- title -->
						<div id="extraContainer1">
							<!--extra user content renders here-->
						</div>
						<!-- extra content -->
					</div>
				</div>
				<div id="wrap-nav">
					<nav id="navigation" class="clearfix">
						<ul class="menu">
							<li>
								<a href="../../index.html" rel="self">首頁 | Home</a>
							</li>
							<li>
								<a href="../../Research/Research.html" rel="self">研究 | Research</a>
								<ul class="menu">
									<li>
										<a href="../../Research/Research/Research_1.html" rel="self">設計+不確定因素
											<br>&nbsp Design+Uncertainty</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_2.html" rel="self">複雜系統+不確定因素
											<br>&nbsp Complex System+Uncertainty</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_3.html" rel="self">動態+規劃
											<br>&nbsp Dynamic+Planning</a>
									</li>
									<li>
										<a href="../../Research/Research/Research_4.html" rel="self">智慧載具+可靠度
											<br>&nbsp Intelligent Vehicle+Reliability</a>
									</li>
								</ul>
							</li>
							<li class="current">
								<a href="../Member/Member.html" rel="self">成員 | Member</a>
								<ul class="menu">
									<li>
										<a href="../../Member/Member/Member.html" rel="self">現任成員 | Current Member</a>
									</li>
									<li>
										<a href="../../Member/Alumni/Alumni.html" rel="self">畢業學生 | Alumni</a>
									</li>
								</ul>
							</li>
							<li>
								<a href="../../Teaching/Teaching.html" rel="self">課程 | Teaching</a>
							</li>
							<li>
								<a href="../../ContactInfo/ContactInfo.html" rel="self">聯絡方式 | Contact info</a>
							</li>
						</ul>
					</nav>
				</div>
				<!-- nav -->
				<div id="header-container">
					<div id="banner">
						<div id="slides">
							<div id="extraContainer2">
								<!--extra user content renders here-->
							</div>
						</div>
						<!-- extra content -->
					</div>
					<!-- banner -->
				</div>
				<!-- header-container -->
			</header>
			<!-- header -->
			<div id="extraContainer3">
				<!--extra user content renders here-->
			</div>
			<div id="main-container">
				<div id="main" class="clearfix">
					<section id="primary-container">
						<span style="font:17px Verdana, serif; font-weight:bold; color:#000000;font-weight:bold; ">Alumni</span>
						<span style="font:17px Verdana, serif; font-weight:bold; font-weight:bold; ">
							<br />
							<br />
						</span>
						<code><table style="line-height:15px"><tr valign=bottom></tr><tr valign=bottom><td></code>
	"""

	script2 = u"""
						<span style="font:12px STHeitiTC-Light; ">
							<a href="{0}" rel="self" title="{1}">{2}</a>
						</span>
						<code><a href="{0}" rel="self" title="{1}"><br></a></code>
						<span style="font:12px Arial, Verdana, Helvetica, sans-serif; ">
							<a href="{0}" rel="self" title="{1}">{1}
								<br>
							</a>
						</span>
						<span style="font:12px Arial, Verdana, Helvetica, sans-serif; ">
							<a href="{0}" rel="self" title="{1}">
								<img class="imageStyle" alt="{1}" src="{3}" width="150" height="113" />
							</a>
						</span>
	"""

	script3_1 = u"""
						<code></td></tr><tr valign=bottom><td></code>
	"""

	script3_2 = u"""
						<code></td><td></code>
	"""

	script4 = u"""
						<code></td></tr></table></code>
					</section>
					<!-- #primary-container -->
					<aside id="secondary-container">
						<h3></h3>
						<div id="sidebar">

						</div>
						<!-- #sidebar -->
						<div id="plugin-sidebar">

						</div>
						<!-- #plugin-sidebar -->
					</aside>
					<!-- #secondary-container -->
				</div>
				<!-- #main -->
			</div>
			<!-- #main-container -->
			<div id="bottom">
				<div id="breadcrumb"></div>
				<!-- #breadcrumb -->
				<div id="extraContainer4">
					<!--extra user content renders here-->
				</div>
			</div>
			<div id="footer-container">
				<footer>
					<p>&copy; 2015 Kuei-Yuan Chan
						<a href="#" id="rw_email_contact">Contact Me</a>
						<script type="text/javascript">var _rwObsfuscatedHref0 = "mai"; var _rwObsfuscatedHref1 = "lto"; var _rwObsfuscatedHref2 = ":ch"; var _rwObsfuscatedHref3 = "ank"; var _rwObsfuscatedHref4 = "y@n"; var _rwObsfuscatedHref5 = "tu."; var _rwObsfuscatedHref6 = "edu"; var _rwObsfuscatedHref7 = ".tw"; var _rwObsfuscatedHref = _rwObsfuscatedHref0 + _rwObsfuscatedHref1 + _rwObsfuscatedHref2 + _rwObsfuscatedHref3 + _rwObsfuscatedHref4 + _rwObsfuscatedHref5 + _rwObsfuscatedHref6 + _rwObsfuscatedHref7; document.getElementById('rw_email_contact').href = _rwObsfuscatedHref;</script>
					</p>
				</footer>
				<!-- footer -->
			</div>
			<!-- #footer-container -->
		</div>
		<!-- #wrap -->
	</body>

	</html>
	"""

class AlumniPage():
	script1 = u"""
						<code></td></tr></table></code>
					</section>
					<!-- #primary-container -->
					<aside id="secondary-container">
						<h3></h3>
						<div id="sidebar">
	"""

	script2_1 = u"""
							<img class="imageStyle" src="{0}" width="300" height="225" />
							<br />
							<span style="font:16px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; ">{1} {2}</span>
							<hr>
	"""

	script2_2 = u"""
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>現職 Present Job</u></span>
							<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
								{1}
							</span>
							<br />
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
								{2} <a href="{0}" rel="external">(Link)</a>
							</span>
							<br /><br /><br />
	"""

	script2_2_1 = u"""
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>現職 Present Job</u></span>
							<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
								{0}
							</span>
							<br /><br />
	"""

	script2_3 = u"""		<br />
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>學歷 Educations</u></span>
							<code><p style="line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">{0}</span>
							<br />
							<code></p></code>
							<br />
	"""

	script2_4 = u"""
							<span style="font:14px Arial, Verdana, Helvetica, sans-serif; font-weight:bold; color:#000000;font-weight:bold; "><u>學位論文 Thesis</u></span>
							<br />
							<code><p style="line-height:15px"></code>
							<span style="font:13px STHeitiTC-Light; ">
								{0}
							</span>
							<code><p style="margin-top: 0.5em;line-height:15px"></code>
							<span style="font:13px Arial, Verdana, Helvetica, sans-serif; color:#000000;">
								{1} <a href="{2}" rel="external">(Link)</a>
							</span>
							<code></p></code>
	"""

	script3 = u"""
						</div>
						<!-- #plugin-sidebar -->
					</aside>
					<!-- #secondary-container -->
				</div>
				<!-- #main -->
			</div>
			<!-- #main-container -->
			<div id="bottom">
				<div id="breadcrumb"></div>
				<!-- #breadcrumb -->
				<div id="extraContainer4">
					<!--extra user content renders here-->
				</div>
			</div>
			<div id="footer-container">
				<footer>
					<p>&copy; 2015 Kuei-Yuan Chan
						<a href="#" id="rw_email_contact">Contact Me</a>
						<script type="text/javascript">var _rwObsfuscatedHref0 = "mai"; var _rwObsfuscatedHref1 = "lto"; var _rwObsfuscatedHref2 = ":ch"; var _rwObsfuscatedHref3 = "ank"; var _rwObsfuscatedHref4 = "y@n"; var _rwObsfuscatedHref5 = "tu."; var _rwObsfuscatedHref6 = "edu"; var _rwObsfuscatedHref7 = ".tw"; var _rwObsfuscatedHref = _rwObsfuscatedHref0 + _rwObsfuscatedHref1 + _rwObsfuscatedHref2 + _rwObsfuscatedHref3 + _rwObsfuscatedHref4 + _rwObsfuscatedHref5 + _rwObsfuscatedHref6 + _rwObsfuscatedHref7; document.getElementById('rw_email_contact').href = _rwObsfuscatedHref;</script>
					</p>
				</footer>
				<!-- footer -->
			</div>
			<!-- #footer-container -->
		</div>
		<!-- #wrap -->
	</body>

	</html>
	"""