function initialize() {
	// body...
	var rows= document.getElementsByClassName("coinRow");
	for(var i= 0; i< rows.length; i++){
		var row= rows[i];
		row.addEventListener("click", function(event){
			var text= event.target.innerHTML;
			var aa= text.split(">")[1];
			window.location = 'coin.php?name='+aa;
		});
	}
}