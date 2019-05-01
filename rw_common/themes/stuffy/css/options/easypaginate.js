/* ------------------------------------------------------------------------------------------------------------------------

	init jQuery scripts

------------------------------------------------------------------------------------------------------------------------ */

$wt=jQuery.noConflict();
$wt(document).ready(function(){
	$wt('div.album-wrapper').easyPaginate({step:photoCount,delay:0});
});

/*
 * 	Easy Paginate 1.0 - jQuery plugin
 *	written by Alen Grakalic	
 *	http://cssglobe.com/
 *
 *	Copyright (c) 2011 Alen Grakalic (http://cssglobe.com)
 *	Dual licensed under the MIT (MIT-LICENSE.txt)
 *	and GPL (GPL-LICENSE.txt) licenses.
 *
 *	Built for jQuery library
 *	http://jquery.com
 *
 */
var photoCount = 10;
(function(a){a.fn.easyPaginate=function(m){var e={step:4,delay:100,numeric:true,nextprev:true,controls:"pagination",current:"current"};var m=a.extend(e,m);var c=m.step;var g,l;var b=a(this).children();var i=b.length;var f,h,d;var j=1;function k(){g=((j-1)*c);l=g+c;a(b).each(function(n){var o=a(this);o.hide();if(n>=g&&n<l){setTimeout(function(){o.fadeIn("fast")},(n-(Math.floor(n/c)*c))*m.delay)}if(m.nextprev){if(l>=i){h.fadeOut("fast")}else{h.fadeIn("fast")}if(g>=1){d.fadeIn("fast")}else{d.fadeOut("fast")}}});a("li","#"+m.controls).removeClass(m.current);a('li[data-index="'+j+'"]',"#"+m.controls).addClass(m.current)}this.each(function(){f=this;if(i>c){var n=Math.floor(i/c);if((i/c)>n){n++}var o=a('<ol id="'+m.controls+'"></ol>').insertAfter(f);if(m.nextprev){d=a('<li class="prev">&laquo;</li>').hide().appendTo(o).click(function(){j--;k()})}if(m.numeric){for(var p=1;p<=n;p++){a('<li data-index="'+p+'">'+p+"</li>").appendTo(o).click(function(){j=a(this).attr("data-index");k()})}}if(m.nextprev){h=a('<li class="next">&raquo;</li>').hide().appendTo(o).click(function(){j++;k()})}k()}})}})(jQuery);