$(function()
{
	$("#TLProduct").change(function(){
		if($(this).find(":selected").val()!="HL"){
			$('#LTVgroup').hide();
		} else {
			$('#LTVgroup').show();
		}

	});
});
