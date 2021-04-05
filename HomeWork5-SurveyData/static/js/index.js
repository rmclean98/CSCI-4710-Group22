function retrieveSurveyData(){
$(document).ready(function() {
    var totalRows = $('#dataTable1').find('tbody tr:has(td)').length;
    var recordPerPage = 25;
    var totalPages = Math.ceil(totalRows / recordPerPage);
    var $pages = $('<div id="pages"><div></div></div>');
    for (i = 0; i < totalPages; i++) {
        $('<span id="span1"><a id="d1' + (i+1) + '">&nbsp;' + (i + 1) + '</a></span>').appendTo($pages);
    }
    $pages.appendTo('#dataTable1');
	$('#d11').css('color', 'black');
    $('.pageNumber').hover( function() {
        $(this).addClass('focus');
    },  function() {
        $(this).removeClass('focus');
    } );
    $('#dataTable1').find('tbody tr:has(td)').hide(); 
    var tr = $('#dataTable1 tbody tr:has(td)'); 
    for (var i = 0; i <= recordPerPage - 1; i++) { 
        $(tr[i]).show();
    }
    $('div span#span1').click(function(event) {
        $('#dataTable1').find('tbody tr:has(td)').hide();
        var nBegin = ($(this).text() - 1) * recordPerPage;
        var nEnd = $(this).text() * recordPerPage - 1;
        for (var i = nBegin; i <= nEnd; i++)  {
            $(tr[i]).show();
        }
		var pageId=$(this).text().trim();
		for (i = 0; i < totalPages; i++) {
		$('#d1' +i).css('color', 'blue');
		}
		$('#d1' + pageId).css('color', 'black');
		
		
		
    });
});



$(document).ready(function() {
    var totalRows = $('#dataTable2').find('tbody tr:has(td)').length;
    var recordPerPage = 25;
    var totalPages = Math.ceil(totalRows / recordPerPage);
    var $pages = $('<div id="pages"></div>');
    for (i = 0; i < totalPages; i++) {
        $('<span id="span2"><a id="d2' + (i+1) + '">&nbsp;' + (i + 1) + '</a></span>').appendTo($pages);
    }
    $pages.appendTo('#dataTable2');
	$('#d21').css('color', 'black');
    $('.pageNumber').hover( function() {
        $(this).addClass('focus');
    },  function() {
        $(this).removeClass('focus');
    } );
    $('#dataTable2').find('tbody tr:has(td)').hide(); 
    var tr = $('#dataTable2 tbody tr:has(td)'); 
    for (var i = 0; i <= recordPerPage - 1; i++) { 
        $(tr[i]).show();
    }
    $('span#span2').click(function(event) {
        $('#dataTable2').find('tbody tr:has(td)').hide();
        var nBegin = ($(this).text() - 1) * recordPerPage;
        var nEnd = $(this).text() * recordPerPage - 1;
        for (var i = nBegin; i <= nEnd; i++)  {
            $(tr[i]).show();
        }
		var pageId=$(this).text().trim();
		for (i = 0; i < totalPages; i++) {
		$('#d2' +i).css('color', 'blue');
		}
		$('#d2' + pageId).css('color', 'black');
		
		
		
    });
});




$(document).ready(function() {
    var totalRows = $('#dataTable3').find('tbody tr:has(td)').length;
    var recordPerPage = 25;
    var totalPages = Math.ceil(totalRows / recordPerPage);
    var $pages = $('<div id="pages"></div>');
    for (i = 0; i < totalPages; i++) {
        $('<span id="span3"><a id="d3' + (i+1) + '">&nbsp;' + (i + 1) + '</a></span>').appendTo($pages);
    }
    $pages.appendTo('#dataTable3');
	$('#d31').css('color', 'black');
    $('.pageNumber').hover( function() {
        $(this).addClass('focus');
    },  function() {
        $(this).removeClass('focus');
    } );
    $('#dataTable3').find('tbody tr:has(td)').hide(); 
    var tr = $('#dataTable3 tbody tr:has(td)'); 
    for (var i = 0; i <= recordPerPage - 1; i++) { 
        $(tr[i]).show();
    }
    $('span#span3').click(function(event) {
        $('#dataTable3').find('tbody tr:has(td)').hide();
        var nBegin = ($(this).text() - 1) * recordPerPage;
        var nEnd = $(this).text() * recordPerPage - 1;
        for (var i = nBegin; i <= nEnd; i++)  {
            $(tr[i]).show();
        }
		var pageId=$(this).text().trim();
		for (i = 0; i < totalPages; i++) {
		$('#d3' +i).css('color', 'blue');
		}
		$('#d3' + pageId).css('color', 'black');
		
		
		
    });
});




$(document).ready(function() {
    var totalRows = $('#dataTable4').find('tbody tr:has(td)').length;
    var recordPerPage = 25;
    var totalPages = Math.ceil(totalRows / recordPerPage);
    var $pages = $('<div id="pages"></div>');
    for (i = 0; i < totalPages; i++) {
        $('<span id="span4"><a id="d4' + (i+1) + '">&nbsp;' + (i + 1) + '</a></span>').appendTo($pages);
    }
    $pages.appendTo('#dataTable4');
	$('#d41').css('color', 'black');
    $('.pageNumber').hover( function() {
        $(this).addClass('focus');
    },  function() {
        $(this).removeClass('focus');
    } );
    $('#dataTable4').find('tbody tr:has(td)').hide(); 
    var tr = $('#dataTable4 tbody tr:has(td)'); 
    for (var i = 0; i <= recordPerPage - 1; i++) { 
        $(tr[i]).show();
    }
    $('span#span4').click(function(event) {
        $('#dataTable4').find('tbody tr:has(td)').hide();
        var nBegin = ($(this).text() - 1) * recordPerPage;
        var nEnd = $(this).text() * recordPerPage - 1;
        for (var i = nBegin; i <= nEnd; i++)  {
            $(tr[i]).show();
        }
		var pageId=$(this).text().trim();
		for (i = 0; i < totalPages; i++) {
		$('#d4' +i).css('color', 'blue');
		}
		$('#d4' + pageId).css('color', 'black');
		
		
		
    });
});

}