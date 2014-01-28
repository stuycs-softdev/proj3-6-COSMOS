
$(document).mousemove(function (e) {
    $("#image").stop().animate( {
	left: e.pageX,
	top. e.pageY
    });
});



/*
=======
>>>>>>> 0c01018225c124be3f7707d76d1668354399d25b
// code that is supposed to make the pet jump after clicking a button
$(document).ready(function(){
  $("button").click(function(){
    $("div").animate({down:'50px'});
    $("div").animate({up:'50px'});
    $("div").animate({down:'50px'});
    $("div").animate({up:'50px'});
  });
});


// code that is supposed to make the pet follow the cursor
$("img").mousemove(function(e){
      $('.follow').css({'top': e.clientY - 20, 'left': e.clientX - 20});
})
*/
