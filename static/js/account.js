$(document).ready(function() {
  
  // Show personal data
  // $("#inputName").value("{{ name }}");
  // $("#inputLastName").value("{{ lastname }}");
  // $("#inputUser").value("{{ user }}");
  // $("#inputEmail").value("{{ email }}");
  var pwd1 = $('#inputPassword1');
  var pwd2 = $('#inputPassword2');
  // var button_changes_attr = ""+$("#button-changes").attr("class");
  
  // For password
  pwd1.on('keyup',function(){
    if($('#p1').val() !== ""){
      pwd2.show(0);
      $("#button-changes").attr("disabled", "true"); 
      $("#button-changes").attr("class", "btn btn-primary disabled");
      $("#button-changes").prop("disabled", true);
      pwd2.attr("class", "form-group has-error");
      $("#match-alert").show();
    }
    else{
      pwd2.hide();
      $("#button-changes").prop("disabled", false);
      $("#button-changes").attr("class", "btn btn-primary");
      $('#p2').val("");
      $("#match-alert").hide();
    }
     
  });
  
  
  
  // No password match
  pwd2.on('keyup',function(){
    if ( $('#p1').val() !== $('#p2').val() ){
      // console.log($('#p1').val() + " - " + $('#p2').val());
      pwd2.attr("class", "form-group has-error");
      $("#button-changes").attr("class", "btn btn-primary disabled");
      $("#button-changes").prop("disabled", true);
      $("#match-alert").show();
      // alert('distintos');
          
    }
    else{
      // console.log($('#p1').val() + " - " + $('#p2').val());
      pwd2.attr("class", "form-group");
      // var button_changes_attr = $("#button-changes").attr("class");
      $("#button-changes").attr("class", "btn btn-primary");
      $("#button-changes").prop( "disabled", false );
      $("#match-alert").hide();
      // console.log($("#button-changes").attr("disabled"));
    }
      
      
  });
  
  // Para deshabilitar la cuenta
  var delete_button = false;
  $('#todisable').on('click', function(event) {
    console.log('to disable');
    $('#op').val("delete");
    delete_button = true;
  });
  
  $('#close').on('click', function(event) {
    
      $('#op').val("modify");
      console.log('clicked close');
    
  });
  
  $('body').on('click' ,function(event) {
    // $('#todisable').on('click', function(event) {
      // delete_button = true;
    // });
    if(!delete_button){
      $('#op').val("modify");
      console.log('clicked body');
      delete_button = false;
    }
    else{
      delete_button = false;
    }
  });

    
});

/*
$(window).load(function() {
    $("#showPwd").click(function(){
    var pwd = $("#inputPassword2").val();
    console.log('raffo : '+pwd);
    });
});
*/