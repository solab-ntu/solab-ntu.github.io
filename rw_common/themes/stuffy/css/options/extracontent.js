/*
 * ExtraContent (jQuery) #
 * AUTHOR:	Adam Merrifield <http://adam.merrifield.ca>
			Giuseppe Caruso <http://www.bonsai-studio.net/>
 * VERSION: r1.4.2
 * DATE: 12-16-10 09:40
 */
$wt=jQuery.noConflict();
$wt(document).ready(function(){var a=function(){var a=10;for(i=1;i<=a;i++){$wt("#myExtraContent"+i+" script").remove();$wt("#myExtraContent"+i).appendTo("#extraContainer"+i)}}()});