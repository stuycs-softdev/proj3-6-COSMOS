
// code that is supposed to edit values
$(function() {
	$("#price").on("input", function() {
		$(this).val($(this).val().replace(/\D/g,""));
	});
});




