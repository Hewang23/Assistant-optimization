$(function(){
	$("#sendmsg").click(function(){
		var value = document.getElementById("content").value;
		if(verifymsg(value)){
			$("#checked_content").append("<br />");
			$("#checked_content").append(value);
			// get_info();
		}else{
			$("#unchecked_content").append("<br />");
			// $("#unchecked_content").append("<span class='onError'></span>");
			$("#unchecked_content").append(value);
		}
	});
	function verifymsg(value){
		return true;
	}
});