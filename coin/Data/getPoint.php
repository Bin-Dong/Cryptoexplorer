<?php
	$name= $_GET["name"];
	$contents= "review".$name.".txt";

	echo json_encode(file($contents));
?>