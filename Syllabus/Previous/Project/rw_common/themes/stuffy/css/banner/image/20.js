/* static image */
$wt=jQuery.noConflict();
$wt(document).ready(function(){
	var imagePath = RwGet.pathto('images/editable_images/','banner_');
 	$wt('<div class="static"><ul class="slides"><li><img src="' + imagePath + '20.jpg" /></li></ul></div>').appendTo('#slides');

});