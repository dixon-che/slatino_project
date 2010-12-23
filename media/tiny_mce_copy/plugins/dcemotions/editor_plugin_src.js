/**
 * $Id: editor_plugin_src.js 520 2008-01-07 16:30:32Z spocke $
 *
 * @author Moxiecode
 * @copyright Copyright © 2004-2008, Moxiecode Systems AB, All rights reserved.
 */

(function() {
	tinymce.create('tinymce.plugins.DCEmotionsPlugin', {
		init : function(ed, url) {
			// Register commands
			ed.addCommand('dcEmotion', function() {
				ed.windowManager.open({
					file : url + '/emotions.htm',
					width : 250 + parseInt(ed.getLang('emotions.delta_width', 0)),
					height : 200 + parseInt(ed.getLang('emotions.delta_height', 0)),
					inline : 1
				}, {
					plugin_url : url
				});
			});

			// Register buttons
			ed.addButton('dcemotions', {title : 'dcemotions.emotions_desc', cmd : 'DCEmotion'});
		},

		getInfo : function() {
			return {
				longname : 'Emotions',
				author : 'Dixon',
				authorurl : 'http://dixon.blogspot.com',
				infourl : '',
				version : "0.1"
			};
		}
	});

	// Register plugin
	tinymce.PluginManager.add('dcemotions', tinymce.plugins.DCEmotionsPlugin);
})();