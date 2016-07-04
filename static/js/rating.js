function post(path, parameters) {
    var form = $('#myform');

    form.attr("method", "post");
    form.attr("action", path);

    $.each(parameters, function(key, value) {
        var field = $('<input></input>');

        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);

        form.append(field);
    });

    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();
}
var j = jQuery.noConflict();
j(document).ready(function(){
	
  j("#minus-button").hide();
  
  // Function Add Movie to List
  j("#add-button").on('click',function() {
      j("#add-button").hide('slow');
      j("#minus-button").show('slow');
  });
  
  // Function Remove Movie from List
  j("#minus-button").on('click',function() {
      j("#minus-button").hide('slow');
      j("#add-button").show('slow');
  });
  
  // Functions for rating 
	var rated = j("#calificacion").text();
	console.log(rated);
	if (rated == '1'){
		j('#rate1').css("color","rgb(39, 130, 228)");
		console.log('1star');
	}
	if (rated == '2'){
		j('#rate1').css("color","rgb(39, 130, 228)");
		j('#rate2').css("color","rgb(39, 130, 228)");
		console.log('2star');
	}
	if (rated == '3'){
		j('#rate1').css("color","rgb(39, 130, 228)");
		j('#rate2').css("color","rgb(39, 130, 228)");
		j('#rate3').css("color","rgb(39, 130, 228)");
		console.log('3star');
	}
	if (rated == '4'){
		j('#rate1').css("color","rgb(39, 130, 228)");
		j('#rate2').css("color","rgb(39, 130, 228)");
		j('#rate3').css("color","rgb(39, 130, 228)");
		j('#rate4').css("color","rgb(39, 130, 228)");
		console.log('4star');
	}
	if (rated == '5'){
		j('#rate1').css("color","rgb(39, 130, 228)");
		j('#rate2').css("color","rgb(39, 130, 228)");
		j('#rate3').css("color","rgb(39, 130, 228)");
		j('#rate4').css("color","rgb(39, 130, 228)");
		j('#rate5').css("color","rgb(39, 130, 228)");
		console.log('5star');
	}
	if (rated == ''){
		j('#rate1').css("color","#888");
		j('#rate2').css("color","#888");
		j('#rate3').css("color","#888");
		j('#rate4').css("color","#888");
		j('#rate5').css("color","#888");
		console.log('0star');
	}
	
  j('.rate').on('click', function(event) {
  	var rate = j(this).data('value');
		// alert(a);
		var url = window.location.href;
		post(''+url+'', {value : ''+rate+''});
  });
  
}
);