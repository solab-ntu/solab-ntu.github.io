/* ------------------------------------------------------------------------------------------------------------------------

	Enable FancyBox

------------------------------------------------------------------------------------------------------------------------ */

$wt=jQuery.noConflict();
$wt(document).ready(function(){
	$wt('.thumbnail-frame').each(function(i,frame) {
		$wt(frame).find('a').attr({
			href: $wt(this).find('img').attr('src').replace(/thumb/i,'full'),
			title: $wt(frame).find('.thumbnail-caption').text(),
			rel: 'rw-photo-gallery'
		}).fancybox({
			'transitionIn'	:	'elastic',
			'transitionOut'	:	'elastic',
			'padding'		:	5,
			'speedIn'		:	400, 
			'speedOut'		:	400,
			'overlayShow'	:	true,
			'overlayOpacity':	0.8,
			'centerOnScroll':	true,
			'hideOnContentClick':	true
		});
	});
});