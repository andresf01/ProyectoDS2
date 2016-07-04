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


// Important code!


$('document').ready(function(){
  $('#movies').on('click','a', function(){
    var what = $(this).data('src');
    // console.log('what:'+what);
    var url = window.location.href;
    if ( what !== undefined){
      $.ajax({
          beforeSend: function(){
            
          },
          url: url,
          type: "POST",
          data: {'op': "delete", 'value': what},
          headers:  {"X-CSRFToken": getCookie("csrftoken")},
          success: function(resp){
            console.log('OK:'+resp);
            $("div[data-src='" + what +"']").remove();
          },
          error: function(jqXHR, estado, error){
            // show error
            // console.log(estado);
            console.log(error);
          },
          complete: function(jqXHR, estado){
            // console.log(estado);
          },
          timeout: 10000
          
        });
    }
  });
  
});


