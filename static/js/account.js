$(window).load(function() {
    // Show personal data
    // $("#inputName").value("{{ name }}");
    // $("#inputLastName").value("{{ lastname }}");
    // $("#inputUser").value("{{ user }}");
    // $("#inputEmail").value("{{ email }}");
    
    
    // No password match
    $("#inputPassword2").attr("class", "form-group has-error");
    var button_changes = $("#button-changes").attr("class");
    $("#button-changes").attr("class", button_changes+" disabled");
    $("#button-changes").attr("disabled", "true");
    
});

$(window).load(function() {
    $("#showPwd").click(function(){
    var pwd = $("#inputPassword2").val();
    console.log('raffo : '+pwd);
    });
});
