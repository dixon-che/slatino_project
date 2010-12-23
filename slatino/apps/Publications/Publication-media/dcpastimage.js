var PastImageDialog = {
	init : function(ed) {
		tinyMCEPopup.resizeToInnerSize();
	},
	insert : function(image_url) {
		image_url_thumbnail = image_url + "300/"
		str_for_past = '<a href="' + image_url + '" target="_blank"><img src="' + image_url_thumbnail + '"></a><br />'

		tinyMCEPopup.execCommand('mceInsertContent', false, str_for_past);
		tinyMCEPopup.close();
	}
};