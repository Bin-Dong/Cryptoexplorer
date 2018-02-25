function initialize(name) {
	// body...
	var xhttp = new XMLHttpRequest();
	var ul= document.getElementById("ul");
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
	var html= "";        
    for(var i= 0; i< data.length; i++){
	html+= "<li class='list-group-item'>"+data[i]+"</li>";
}
	ul.innerHTML= html;
        }
    };
    xhttp.open("GET", "Data/getPoint.php?name="+name, true);
    xhttp.send();
}
function submitComment(){
	var comment= document.getElementById("comment").value;
	var innerHTML= document.getElementById("ul").innerHTML;
	document.getElementById("ul").innerHTML= innerHTML+"<li class='list-group-item'>"+comment+"</li>";
}