$( document ).ready(function() {

	$( "#id_actual_time" ).blur(function() {
		//get value of the "actual time" input
		actualTime = $( "#id_actual_time").val();

		//if there is something in the box
		if (actualTime != " "){
			//split the hours and minutes into an array
			var newTime = actualTime.split(":");
			
			//cost is $3 per hour
			var hourCost = (parseInt(newTime[0],10)) * 3;
			
			//plus $0.05 per minute
			var minuteCost = (parseInt(newTime[1],10)) * 0.05;
			
			//add them up
			cost = hourCost + minuteCost;
			
			//typeOf(cost) returns NaN if you don't enter it with a colon
			if (isNaN(cost)){
				alert("Please time enter in HH:MM format");
			}

			//minimum cost is $3
			if (cost < 3){
				cost = 3;
			}

			//return cost with two decimals
			cost = cost.toFixed(2);

			//fill in the actual cost input
			$("#id_job_cost").val(cost);
		}
	});


	$( "#id_estimated_time" ).blur(function() {
		estimatedTime = $( "#id_estimated_time").val();
		if (estimatedTime != " "){
			var newTime = estimatedTime.split(":");
			var hourCost = (parseInt(newTime[0],10)) * 3;
			var minuteCost = (parseInt(newTime[1],10)) * 0.05;
			cost = hourCost + minuteCost;
			
			if (isNaN(cost)){
				alert("Please time enter in HH:MM format");
			}
			
			if (cost < 3){
				cost = 3;
			}
			
			cost = cost.toFixed(2);
			
			$("#id_estimated_cost").val(cost);
			
			$( "#id_estimated_time" ).blur(function() {
				window.print();
			});
		}
	});
});