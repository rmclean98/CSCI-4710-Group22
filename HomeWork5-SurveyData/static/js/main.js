	  
 function retrieveSurveyData(){
	  $(document).ready(function () { 
		if (localStorage.getItem("repoObject") != null) {
  data=JSON.parse(localStorage.getItem("repoObject"));
  $('#table_div').empty();
	// var magic
	var student='';
	student+=`<table class="table" id="table" ><caption>Vampire Test Results by Rule Based Method</caption><thead>
  <tr>
	<th>Firstname</th>
	<th>Middlename</th>
	<th>Lastname</th>
	<th>Gender</th>
	<th>Garlic</th>
	<th>Pale</th>
	<th>Shadow</th>
	<th>Result</th>
  </tr>
</thead>`;

	
	$.each(data, function (key, value) { 
	


	 student += '<tr>'; 
						student += '<td>' +  
							value.FirstName + '</td>'; 

						student += '<td>' +  
							value.MiddleName + '</td>'; 

						student += '<td>' +  
							value.LastName + '</td>'; 

						student += '<td>' +  
							value.Gender + '</td>'; 
							
						student += '<td>' +  
							value.Garlic + '</td>'; 
							
						student += '<td>' +  
							value.Shadow + '</td>'; 
							
						student += '<td>' +  
							value.Pale + '</td>'; 
							
						student += '<td>' +  
						value.Result + '</td>'; 

					  //INSERTING ROWS INTO TABLE  
					student += '</tr>';    
					}); 
					  
				   
						
					student += '</table>';	
						
					$('#table_div').append(student); 
			   
		}
		else{
			$('#table_div').empty();
			var student='';
	student+=`<table class="table" id="table" ><caption>Vampire Test Results by Rule Based Method</caption><thead>
  <tr>
	<th>Firstname</th>
	<th>Middlename</th>
	<th>Lastname</th>
	<th>Gender</th>
	<th>Garlic</th>
	<th>Pale</th>
	<th>Shadow</th>
	<th>Result</th>
  </tr>
</thead> </table><br>
<p style="text-align:center;"> No Records </p>;`;
$('#table_div').append(student);
		}
	});
  }
	  
	  
	 
	  
	  
	  
	  
	  
	 

