// For cookie (AJAX)
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



// Funcion para generar el html de cada lista
function getList(link, name){
  var text=""
  
  text = "<div id=\"item-list\" class=\"row\" data-src=\""+link+"\"><div class=\"col-xs-11 col-sm-11 col-md-11 col-lg-11\"><li class=\"list\"><a href=\""+link+"\">"+name+"</a></li></div><div class=\"col-xs-1 col-sm-1 col-md-1 col-lg-1 text-center\"><a data-src=\""+link+"\"><span class=\"glyphicon glyphicon-remove\"></span></a></div></div>";
  
  return text;
}

$('document').ready(function() {
  // Objeto DOM del campo de insercion
  var newList = $('#name-new-list');
  // Objeto DOM del boton 
  var buttonList = $('#addlist-button');
  
  // Evitar enter
  $("#name-new-list").keypress(function(e) {
    if (e.which == 13) {
      return false;
    }
  });
  
  // Bloquear y desbloquear el boton en funcion de que haya texto en el input
  newList.on('keyup', function(){
    if (newList.val() != "")
    {
      enableItem('#addlist-button');
    }
    else
    {
      disableItem('#addlist-button');
    }
  } );
  // Al dar clic en el boton de agregar
  // Agregar item en la lista, limpiar el campo y volver a bloquear el boton de agregar
  buttonList.on('click',function (){
    var titulo = newList.val();
    var url = window.location.href;
    // para pruebas
    // $('#listas').append(getList('calavera',titulo));
    // newList.val('');
    // disableItem('#addlist-button');
    // fin para pruebas
    
    $.ajax({
      beforeSend: function(){
        // var rated = $("#calificacion").text();
        // console.log(rated);
        // setRating(rated);
      },
      url: url,
      type: "POST",
      data: {'op': "create", 'value': titulo},
      headers:  {"X-CSRFToken": getCookie("csrftoken")},
      success: function(resp){
        console.log('OK:'+resp);
        $('#listas').append(getList(resp,titulo));
        newList.val('');
        disableItem('#addlist-button');
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
    
  });
  
  
  // Al dar clic en la 'x' correspondiente a una lista
  // Se elimina la lista correspondiente de la base de datos del usuario
  // y se actualiza la vista, indicando la eliminación correcta
  $('#listas').on('click', 'a',function() {
    // Que item va a ser eliminado
    var what = $(this).data('src');
    // console.log("id: "+what);
    var url = window.location.href;
    
    // We can use confirm method for ask to a confirmation from user
    
    // para pruebas
    // console.log(what);
    // $("div[data-src='" + what +"']").remove();
    // fin para pruebas
    if ( what !== undefined){
      //console.log("verified");
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