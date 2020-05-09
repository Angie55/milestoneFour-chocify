$(document).ready(function () {
 
window.setTimeout(function() {
    $(".alert").fadeTo(1000, 0).slideUp(1000, function(){
        $(this).remove(); 
    });
}, 5000);

$(".prod-thumb img").hover(function(){
    $('#main-img').attr('src',$(this).attr('src').replace(/['"]?\)$/,''));
});

$('.prod-thumb').click(function() {
        let url = $(this).attr('src').replace(/^url\(['"]?/,'').replace(/['"]?\)$/,'');
        $('#main-img').attr('src', url);
    });

});
