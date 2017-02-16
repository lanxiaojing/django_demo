

function get_sub(src, max) {
	if (src.length >= max) {
		return src.substr(0, max) + "...";
	}
	return src;
}


function generate_weixin_bindcode(control) {
	$.getJSON("/rest/weixin/generate_bindcode/", {}, function(data){
		if (data["is_ok"] == false) {
			control.innerHTML = "生成绑定码失败，重新生成";
		} else {
			control.innerHTML = data["code"]; 
		}
	});
}


function typeahead(ctrl, url, params) {
	$.getJSON(url, params, function(data) {
		if (data["is_ok"] == false) {
			return;
		}
		function extractor(query) {
		    var result = /([^,]+)$/.exec(query);
		    if(result && result[1])
		        return result[1].trim();
		    return '';
		}
		
		$('#' + ctrl.id).typeahead({
		    source: data["result"]
		});
	});
}