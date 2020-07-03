function sendCommand(){
	var content = document.getElementById("content").value;
	var unchecked_content = document.getElementById("unchecked_content");
	var up = document.createElement("p");
	var utextNode = document.createTextNode(content);
	up.appendChild(utextNode);
	//----------华丽的分割线----------
	var checked_content = document.getElementById("checked_content");
	var p = document.createElement("p");
	var textNode = document.createTextNode(get_info());
	p.appendChild(textNode);
			
	if(excuteCommand()){
		checked_content.append(p);
	}else{
		unchecked_content.appendChild(up);
	}
}
function excuteCommand(){ 
	return false;
}