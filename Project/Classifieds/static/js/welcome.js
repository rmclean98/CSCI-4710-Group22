$(document).ready(function() {
$('#loginModal').modal('hide');

//if (getCookie('UserCreated')=='Yes'){
//$(document).find('#newusersuccessful').show()
//document.cookie = "UserCreated=" + 'No';
//document.cookie = "expires=" + now.toUTCString() + ";"
//}
//else{
//$(document).find('#newusersuccessful').hide()
//}


$(document).find('button#login_button.btn.btn-info.btn-block.btn-round').click(function() {
    $('#loginModal').modal('show');
  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })
});

$(document).find('button#loginbutton.btn.btn-info.btn-block.btn-round').click(function(){
    $.ajax({
            url: 'http://127.0.0.1:5287/classifieds/login/',
            type: "POST",
			contentType: "application/json; charset=utf-8",
			data: '{"username":"' + $("#emailTextBox").val() + '","password":"' + $("#passwordTextBox").val() + '"}',
            
            success: function(data) {
				
				//var obj = JSON.parse(data1);
					if (getCookie('Authenticated')=='Yes'){
						$('#loginModal').modal('hide');
						location.reload();
					}
					else{
						var $error = $('<p>Username or Password is incorrect</p>');
						$error.appendTo('#errormsg');
					}
					//if (data1.loginStatus == 'Successful') { //if your response have 'status' key
					//location.reload();
					//temp=$.session.get('username')
					console.log(data)
					//var url = "/classifieds";    
					//$(location).attr('href',url)
					
					//$(document).replaceWith(data1.form);
                   
                //} else {
                  // alert('Error.');
                
            }
        });
		
	
});




$(document).find('a#signup_link').click(function(){
    $.ajax({
            url: 'http://127.0.0.1:5287/classifieds/Register/',
            type: "GET",
			            
            success: function(data) {
				
				//var obj = JSON.parse(data1);
					
						$('#loginModal').modal('hide');
						
					console.log(data)
					//var url = "/classifieds";    
					//$(location).attr('href',url)
					
					//$(document).replaceWith(data1.form);
                   
                //} else {
                  // alert('Error.');
                
            }
        });
		
	
});







});



function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}




