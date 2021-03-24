function is_vampire(){
var selectItem = document.getElementById("mySelect");
var selectedMethod = selectItem.options[selectItem.selectedIndex].text;
if (selectedMethod=='Random Guess'){
is_vampire_ByRandom()
}
else{
is_vampire_ByCriteria()
}
}


function change_Logic(){
var selectItem = document.getElementById("myChangeSelect");
var selectedMethod = selectItem.options[selectItem.selectedIndex].text;
if (selectedMethod=='Random Guess'){
update_Table_ByRandom();
update_Chart_ByRandom();
}
else{
update_Table_ByCriteria();
update_Chart_ByCriteria();
}
}


function is_vampire_ByCriteria(){
        // var magic
		result=0;
		garlic='';
		Pale='';
		shadow='';
		var Gender='';
		var genders = document.getElementsByName("optradio");
		
		
		for(var i = 0; i < genders.length; i++) {
		if(genders[i].checked)
		Gender = genders[i].id;
		}
        if(document.getElementById('garlic_checkbox').checked == false){
          result=result+3;
		  garlic="False";
        }
		else{
			garlic="True"
		}
		
		 if(document.getElementById('shadow_checkbox').checked == false){
          result=result+4;
        
		 shadow="False"
        }
		else{
			shadow="True"
		}
		
		if(document.getElementById('complexion_checkbox').checked == true){
          result=result+3;
        
		 pale="False"
        }
		else{
			pale="True"
		}
		
		
		
        if(result <= 6){
          
		  if (localStorage.getItem("repoObject") != null) {
				var repoObj=JSON.parse(localStorage.getItem("repoObject"));
				repoObj.push({"FirstName": document.getElementById('first_name').value,
				"MiddleName":document.getElementById('middle_name').value,				
				"LastName":document.getElementById('last_name').value,
				"Gender":Gender,
				"Garlic":garlic,
				"Shadow":shadow,
				"Pale":pale,
		  "Result":"Human"});
				localStorage.setItem('repoObject', JSON.stringify(repoObj));	
			}
			else{
				var repoObj=[]
				//var repoObj=new Object()
				repoObj.push({"FirstName": document.getElementById('first_name').value,
				"MiddleName":document.getElementById('middle_name').value,				
				"LastName":document.getElementById('last_name').value,
				"Gender":Gender,
				"Garlic":garlic,
				"Shadow":shadow,
				"Pale":pale,
				"Result":"Human"});
				
				localStorage.setItem('repoObject', JSON.stringify(repoObj));		
			}
		  
          alert("is a Human");
		
	  
        }
        else {
				 if (localStorage.getItem("repoObject") != null) {
				var repoObj=JSON.parse(localStorage.getItem("repoObject"));
				repoObj.push({"FirstName": document.getElementById('first_name').value,
				"MiddleName":document.getElementById('middle_name').value,				
				"LastName":document.getElementById('last_name').value,
				"Gender":Gender,
				"Garlic":garlic,
				"Shadow":shadow,
				"Pale":pale,
				"Result":"Vampire"});
				localStorage.setItem('repoObject', JSON.stringify(repoObj));	
			}
			else{
				var repoObj=[]
				//var repoObj=new Object()
				repoObj.push({"FirstName": document.getElementById('first_name').value,
				"MiddleName":document.getElementById('middle_name').value,				
				"LastName":document.getElementById('last_name').value,
				"Gender":Gender,
				"Garlic":garlic,
				"Shadow":shadow,
				"Pale":pale,
				"Result":"Vampire"});
				
				localStorage.setItem('repoObject', JSON.stringify(repoObj));		
			}
		  alert("is a Vampire");
			
          
        }
		
		update_Table_ByCriteria();
		update_Chart_ByCriteria();
      }
	  
	  
	  function update_Table_ByCriteria(){
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
	  
	  
	  function update_Chart_ByCriteria(){
		  
	// Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(draw_Chart_ByCriteria);
	  }
	  
	 function draw_Chart_ByCriteria(){ 
	 var chart;
      var chartData;
      var options;
      var num_human=0;
      var num_vampire=0;
	  // Create the data table.
        chartData = new google.visualization.DataTable();
        chartData.addColumn('string', 'Element');
        chartData.addColumn('number', 'Number');
        chartData.addRows([
          ['Human', num_human],
          ['Vampire', num_vampire]
        ]);

        // Set chart options
        options = {'title':'Rule Based Results-Pie Chart',
                       'width':400,
                       'height':300};

       
		  
		
			if (localStorage.getItem("repoObject") != null) {
	  data=JSON.parse(localStorage.getItem("repoObject"));  
        // var magic
		result=0;
		
		$.each(data, function (key, value) { 
        if(value.Garlic == "False"){
          result=result+3;
        }
		
		 if(value.Shadow  == "False"){
          result=result+4;
        }
		
		if(value.Complexion== "True"){
          result=result+3;
        }
		
        if(result <= 6){
          //window.alert("Only two vampires left. Mercy please.");
          //num_vampire -= 1;
          //num_human = parseInt(localStorage.getItem('num_human_local')) + 1;
		   num_human = num_human + 1;          
        }
        else {
          //num_vampire = parseInt(localStorage.getItem('num_vampire_local'))+1;
		  
		  num_vampire = num_vampire+1;
		  
          
          //chart.draw(chartData, options);
        }
		
		});
			}
		
		
		//data.removeRow(1);
          chartData.removeRow(0);
		 //total_rows=data.getNumberOfRows
          chartData.insertRows(0, [['Human', num_human]]);   
			
          chartData.removeRow(1);
          //data.removeRow(0);
          
          chartData.insertRows(1, [['Vampire', num_vampire]]);
		  
        chart = new google.visualization.PieChart(document.getElementById('chart_div'));
		chart.draw(chartData, options);
		
		
		
		
		 
      }
	  
	  
	  
	  
	  
	  
	 

