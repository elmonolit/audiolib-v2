$(document).ready(function () {
    $("h3").hover( function () { //tag
        $(this).css('color','red');
        },
    function () {
        $(this).css('color','blue');
        });
    $("#search").keyup( function(){
        var query;
        query = $(this).val();
        $.get('/search/', {search: query}, function(data){
            $('#bands_search').html(data);
            });
        });
})