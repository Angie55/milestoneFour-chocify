$(document).ready(function () {
    
// Code to automatically fade the alert message 
window.setTimeout(function() {
    $(".alert").fadeTo(1000, 0).slideUp(1000, function(){
        $(this).remove(); 
    });
}, 5000);

// Code for product_details page so thumbnails can be clicked to make them the main, larger image.
$('.prod-thumb').click(function() {
        let url = $(this).attr('src').replace(/^url\(['"]?/,'').replace(/['"]?\)$/,'');
        $('#main-img').attr('src', url);
    });

});
