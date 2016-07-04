$(window).load(function() {
    $("#full-screen").hide();
    $("#main-content").show();
    $("#myfooter").show();
    $("#header-content").show("fast");
});

/*$('body').on('click', function (e) {
    $('[data-toggle="popover"]').each(function () {
        //the 'is' for buttons that trigger popups
        //the 'has' for icons within a button that triggers a popup
        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
            $(this).popover('hide');
        }
    });
});*/

function disableItem(itemID){
    $(''+itemID).prop("disabled", true);
}

function enableItem(itemID){
    $(''+itemID).prop("disabled", false);
}