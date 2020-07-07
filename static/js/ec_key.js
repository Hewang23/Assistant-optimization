$(function(){
	// $("#content").after("<font>*</font>")
	$("#content").keyup(function(){
		var value = $(this).val();
		$(".onError").remove();
		$(".onSuccess").remove();
		if(value.length>10||value.length<3){
			$(this).parent().append("<span class='onError'>命令行格式有误</span>")
		}else{
			$(this).parent().append("<span class='onSuccess'>命令行格式正确</span>")
		}
	}).blur(function(){
		$(".onError").remove();
		$(".onSuccess").remove();
	});
});