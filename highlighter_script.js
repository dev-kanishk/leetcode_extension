
setTimeout(function() {
	for(var i = 0; i < questions.length; i++){
		var x = document.querySelectorAll("td[value='"+questions[i]+"']");
		if (x.length > 0){
			flag = false;
			x[0].innerHTML = x[0].innerHTML.replace(questions[i], "<mark><b>"+questions[i]+"</b></mark>"); 
		}
	}
}, 10000);
