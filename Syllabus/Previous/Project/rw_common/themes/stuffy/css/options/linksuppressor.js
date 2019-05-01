// Link Suppressor script by Will Woodgate - visit http://www.willwoodgate.com/ for more information
$wt=jQuery.noConflict();
$wt(document).ready(function(){
	$wt("#navigation li:has(ul)").hover(function() {
		$wt(this).children("a").addClass("nolink").click(function(e) {
			e.preventDefault();
		});
	});
});