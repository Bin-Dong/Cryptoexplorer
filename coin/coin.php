<?php
	$name= $_GET["name"];

?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> 
	<script src="https://d3js.org/d3.v4.min.js"></script>
	<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
	<script src= "coin.js"></script>
</head>

<body onload= "initialize('<?php echo $name; ?>')">
	<div class="container">
		
		<ul class="list-group" id='ul'>
		</ul>

		<form>
		  <div class="form-group">
			  <label for="comment">Write Comment:</label>
			  <textarea class="form-control" rows="5" id="comment"></textarea>
			</div> 
		  <div class="btn btn-default" onclick="submitComment()">Submit</div>
		</form> 
	</div>
</body>
</html>