$(function()
{
    $('#div_TLltv').hide();
	$('#TLrecurr').hide();
    $('#div_ODCCltv').hide();
	$('#ODCCrecurr').hide().prop('required',false);
	$tlmagic = function(){
		if (['HL', 'Corporate', 'SME', 'AIB'].includes($("#TLproduct").find(":selected").val())){
		$('#magicdiv1').removeClass('col-sm-12').addClass('col-sm-7')   ;
            $('#magicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
            $('#magicdiv4').show();
            if($('#TLproduct').find(":selected").val()=="HL"){
                $('#div_TLltv').show();
                $('#TLltv').prop('required',true);
                $('#div_TLrating').hide();
                $('#TLrating').prop('required',false);

            } else {
                $('#div_TLrating').show();
                $('#TLrating').prop('required',true);
                $('#div_TLltv').hide();
                $('#TLltv').prop('required',false);
            };
        } else{
            $('#magicdiv1').removeClass('col-sm-7').addClass('col-sm-12');
            $('#magicdiv2').removeClass('col-sm-5').addClass('col-sm-6');
            $('#magicdiv4').hide();
        };
	    if($("#TLproduct").find(":selected").val()=="LAP"){
	        $('#rrp').show();
	    } else{
	        $('#rrp').hide();
	    };	
	};
	$odccmagic = function(){
	    if(['HL', 'Corporate', 'SME', 'AIB'].includes($('#ODCCproduct').find(":selected").val())){
		    $('#odccmagicdiv1').removeClass('col-sm-12').addClass('col-sm-7')   ;
		    $('#odccmagicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
		    $('#odccmagicdiv4').show();
		    if($('#ODCCproduct').find(":selected").val()=="HL"){
		        $('#div_ODCCltv').show();
				$('#ODCCltv').prop('required',true);
		        $('#div_ODCCrating').hide();
		        $('#ODCCrating').prop('required',false)
		    } else {
		        $('#div_ODCCrating').show();
		        $('#ODCCrating').prop('required',true)
		        $('#div_ODCCltv').hide();
		        $('#ODCCltv').prop('required',false);
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

	};
	$tlmagic();
	$odccmagic();
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
		$tlmagic();
	});
	$("#ODCCproduct").change(function(){
		$odccmagic()
	});

});
