$( document ).ready(function() {
	$("#invoice-submit").click(function() {
		console.log($( "#id_job_state option:selected" ).text());
	});


    //( "#id_job_state option:selected" ).text();
    //console.log( $( "#id_job_state option:selected" ).text());
    //if ($( "#id_job_state option:selected" ).text() == "queued"){console.log("queued");}

	

	$( "#id_actual_time" ).blur(function() {
		actualTime = $( "#id_actual_time").val();
		console.log(actualTime);
		if (actualTime != " "){
			console.log("Not zero");
			var newTime = actualTime.split(":");
			console.log(newTime);
			var hourCost = (parseInt(newTime[0],10)) * 3;
			//hourCost = hourCost.toFixed(2);
			var minuteCost = (parseInt(newTime[1],10)) * 0.05;
			//minuteCost = minuteCost.toFixed(2);
			cost = hourCost + minuteCost;
			if (isNaN(cost)){
				alert("Please time enter in HH:MM format");
			}
			console.log(cost);
			if (cost < 3.00){
				cost = 3.00;
			}
			cost = cost.toFixed(2);
			console.log(cost);
			$("#id_job_cost").val(cost);
		}
	});


	$( "#id_estimated_time" ).blur(function() {
		estimatedTime = $( "#id_estimated_time").val();
		console.log(estimatedTime);
		if (estimatedTime != " "){
			console.log("Not zero");
			var newTime = estimatedTime.split(":");
			console.log(newTime);
			var hourCost = (parseInt(newTime[0],10)) * 3;
			//hourCost = hourCost.toFixed(2);
			var minuteCost = (parseInt(newTime[1],10)) * 0.05;
			//minuteCost = minuteCost.toFixed(2);
			cost = hourCost + minuteCost;
			if (isNaN(cost)){
				alert("Please time enter in HH:MM format");
			}
			console.log(cost);
			if (cost < 3.00){
				cost = 3.00;
			}
			cost = cost.toFixed(2);
			console.log(cost);
			$("#id_estimated_cost").val(cost);
		}
	});
});