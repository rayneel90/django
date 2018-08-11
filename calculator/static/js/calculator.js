$(function()
{
    $('#div_TLltv').hide();
	$('#TLrecurr').hide();
    $('#div_ODCCltv').hide();
	$('#ODCCrecurr').hide();
    $(":button.w-100").click(function(){
        $(this).find("i").toggleClass("fa-caret-down");
        $(this).find("i").toggleClass("fa-caret-up")
    }); // For expand-collapse glyph

	$('#TLother').change(function(){
		if( $(this).val()>0){
			$('#TLrecurr').show();
		} else{
			$('#TLrecurr').hide();
		}

	});
	$('#ODCCother').change(function(){
		if( $(this).val()>0){
			$('#ODCCrecurr').show();
		} else{
			$('#ODCCrecurr').hide();
		}

	});
	$("#TLproduct").change(function(){
	    if(['HL', 'Corporate', 'SME', 'AIB'].includes($(this).find(":selected").val())){
		    $('#magicdiv1').removeClass('col-sm-12').addClass('col-sm-7')   ;
            $('#magicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
            $('#magicdiv4').show();
            if($(this).find(":selected").val()=="HL"){
                $('#div_TLltv').show();
                $('#div_TLrating').hide();
            } else {
                $('#div_TLrating').show();
                $('#div_TLltv').hide();
            };
        } else{
            $('#magicdiv1').removeClass('col-sm-7').addClass('col-sm-12');
            $('#magicdiv2').removeClass('col-sm-5').addClass('col-sm-6');
            $('#magicdiv4').hide();
        };
        if($(this).find(":selected").val()=="LAP"){
            $('#rrp').show();
        } else{
            $('#rrp').hide();
        }
	});
	$("#ODCCproduct").change(function(){
	    if(['HL', 'Corporate', 'SME', 'AIB'].includes($(this).find(":selected").val())){
		    $('#odccmagicdiv1').removeClass('col-sm-12').addClass('col-sm-7')   ;
            $('#odccmagicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
            $('#odccmagicdiv4').show();
            if($(this).find(":selected").val()=="HL"){
                $('#div_ODCCltv').show();
                $('#div_ODCCrating').hide();
            } else {
                $('#div_ODCCrating').show();
                $('#div_ODCCltv').hide();
            };
        } else{
            $('#odccmagicdiv1').removeClass('col-sm-7').addClass('col-sm-12');
            $('#odccmagicdiv2').removeClass('col-sm-5').addClass('col-sm-6');
            $('#odccmagicdiv4').hide();
        };
        if($(this).find(":selected").val()=="LAP"){
            $('#odccrrp').show();
        } else{
            $('#odccrrp').hide();
        }
	});

});
