
tinymce.create('tinymce.plugins.PastImagePlugin', {

	init : function(ed, url) {
		var dc_ed_id = ed.id;
        var ed_id_bits = dc_ed_id.split("-");
        var dom_id_base = ed_id_bits[0] + "-" + ed_id_bits[1] + "-" + "base";
        var dc_base_id = document.getElementById(dom_id_base).value;
		if (dc_base_id){
			ed.addCommand('dcPastImageCmd', function() {
				ed.windowManager.open({
					file : '/publication/' + dc_base_id + '/past_image/',
                    title : 'Past image',
                    width : 640,
                    height : 480,
                    scrollbars : true
                    })
                });
            ed.addButton('dcpastimagebuttom', {
                title : 'Past Image',
                image : '/Publication-media/image.gif',
                cmd : 'dcPastImageCmd'
                });
            }
        },
    getInfo : function() {
        return {
            longname : 'Past image plugin',
            author : 'Dixon Che',
            authorurl : 'http://dixon-che.blogspot.com',
            infourl : '',
            version : "0.01"
        };
    }
});
// Register plugin
tinymce.PluginManager.add('dcpastimage', tinymce.plugins.PastImagePlugin);
// Main textarea config
tinyMCE.init({
    width : "640",
    mode : "textareas",
    theme : "advanced",
    plugins : "table,save,advhr,advimage,advlink,dcemotions,-dcpastimage,iespell,insertdatetime,searchreplace,print,contextmenu",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    auto_resize : true,
    theme_advanced_resizing : true,
    theme_advanced_resize_horizontal : false,
    theme_advanced_buttons1 : "cut,copy,paste,separator,undo,redo,separator,search,replace,separator,code,separator,cleanup,separator,bold,italic,underline,strikethrough,separator,forecolor,backcolor,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,help",
    theme_advanced_buttons2 : "removeformat,formatselect,fontselect,fontsizeselect,separator,bullist,numlist,outdent,indent,separator,link,unlink,anchor,separator,dcpastimagebuttom,dcemotions",
    theme_advanced_buttons3 : "sub,sup,separator,image,insertdate,inserttime,separator,tablecontrols,separator,hr,advhr,visualaid,separator,charmap,iespell,separator,print",
    convert_urls : false,
    relative_urls : false,
    plugin_insertdate_dateFormat : "%m/%d/%Y",
    plugin_insertdate_timeFormat : "%H:%M:%S",
    extended_valid_elements : "a[name|href|title|onclick|target],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]"
});
