
// Otra pagina

function sameOrigin(url) {
  // test that a given url is a same-origin URL
  // url could be relative or scheme relative or absolute
  var host = document.location.host; // host + port
  var protocol = document.location.protocol;
  var sr_origin = '//' + host;
  var origin = protocol + sr_origin;
  // Allow absolute or scheme relative URLs to same origin
  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
    // or any other URL that isn't scheme relative or absolute i.e relative.
    !(/^(\/\/|http:|https:).*/.test(url));
}
  
  // usando jQuery
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


function csrfSafeMethod(method) {
  // estos métodos no requieren CSRF
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function itemWithTimer(id, tiempo){
  $(id).show();
  setTimeout(function() { $(id).hide(); }, tiempo*1000);
}

// setRating permite pintar colores al dar clic
function setRating(rated){
  // console.log("vacio: "+ rated);
  if (rated == '1'){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","#888");
    $('#rate3').css("color","#888");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
    // console.log('1star');
  }
  if (rated == '2'){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","#888");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
    // console.log('2star');
  }
  if (rated == '3'){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
    // console.log('3star');
  }
  if (rated == '4'){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","rgb(39, 130, 228)");
    $('#rate5').css("color","#888");
    // console.log('4star');
  }
  if (rated == '5'){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","rgb(39, 130, 228)");
    $('#rate5').css("color","rgb(39, 130, 228)");
    // console.log('5star');
  }
  if (rated == '0'){
    $('#rate1').css("color","#888");
    $('#rate2').css("color","#888");
    $('#rate3').css("color","#888");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
    // console.log('0star');
  }
}

$(document).ready(function(){
  // Defaults
  $('#msg-container').hide();
  $('#msg-container2').hide();
  
  // Change color when mouse is over
  $('#rate1').mouseover(function(){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","#888");
    $('#rate3').css("color","#888");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
  });
  
  $('#rate2').mouseover(function(){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","#888");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
  });
  
  $('#rate3').mouseover(function(){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","#888");
    $('#rate5').css("color","#888");
  });
  
  $('#rate4').mouseover(function(){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","rgb(39, 130, 228)");
    $('#rate5').css("color","#888");
  });
  
  $('#rate5').mouseover(function(){
    $('#rate1').css("color","rgb(39, 130, 228)");
    $('#rate2').css("color","rgb(39, 130, 228)");
    $('#rate3').css("color","rgb(39, 130, 228)");
    $('#rate4').css("color","rgb(39, 130, 228)");
    $('#rate5').css("color","rgb(39, 130, 228)");
  });
  
  $('.rate').mouseout(function(){
    setRating($("#calificacion").text());
  });
  
  // Set rating taked when refresh
  setRating($('#calificacion').text());
  
  // Set rating when a star clicked
  $('.rate').on('click', function(e){
    e.preventDefault();
    // var csrftoken = getCookie('csrftoken');
    var rate = $(this).data('value');
    // $('#var-rate').val(rate);
    // console.log('clicked: ' + rate);
    var url = window.location.href;
    
    // var method_type = $('#myform').attr('method');
    var method_type = 'POST';
    // var action = $('#myform').attr('action');
    var action = url;
    // var my_data = $('#myform').serialize();
    // console.log(action);
    $.ajax({
      beforeSend: function(){
        // var rated = $("#calificacion").text();
        // console.log(rated);
        // setRating(rated);
      },
      url: action,
      type: method_type,
      data: {'op': 'calificar', 'value': rate},
      headers:  {"X-CSRFToken": getCookie("csrftoken")},
      success: function(resp){
        $("#calificacion").text(rate);
        // console.log($('#calificacion').text());
        setRating(""+rate);
      },
      error: function(jqXHR, estado, error){
        // show error
        // console.log(estado);
        // console.log(error);
        setRating($("#calificacion").text());
      },
      complete: function(jqXHR, estado){
        // console.log(estado);
      },
      timeout: 10000
      
    });
  });
  
  // Hide minus button
  
  // $("#minus-button").hide();
  
  // Function Add Movie to List
  /*$("#add-button").on('click',function() {
      $("#add-button").hide('slow');
      $("#minus-button").show('slow');
  });
  */  
  // Function Remove Movie from List
  /*$("#minus-button").on('click',function() {
      $("#minus-button").hide('slow');
      $("#add-button").show('slow');
  });*/
  
  // Add actual movie to selected list
  $('#list').on('click', 'a', function(){
    var what_list = $(this).data('src');
    var url = window.location.href
    var id_movie = url.split("/");
    id_movie = id_movie[id_movie.length-1];
    
    console.log("id lista:" + what_list + " id pelicula: " + id_movie);
    
    $.ajax({
      beforeSend: function(){
        
      },
      url: url,
      type: 'POST',
      data: {'op': 'agregar', 'value': what_list},
      headers:  {"X-CSRFToken": getCookie("csrftoken")},
      success: function(resp){
        // show success message
        $('#myLists').modal('hide');
        $('#msg').text('Successfull');
        // show for a t time
        itemWithTimer('#msg-container', 2.5);
      },
      error: function(jqXHR, estado, error){
        // console.log(estado);
        console.log(error);
        $('#myLists').modal('hide');
        $('#msg2').text('Error, movie didn\'t add');
        // show for a t time
        itemWithTimer("#msg-container2",2.5);
      },
      complete: function(jqXHR, estado){
        // console.log(estado);
      },
      timeout: 10000
      
    });
    
  });
});
  