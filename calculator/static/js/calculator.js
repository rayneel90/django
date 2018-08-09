$(function()
{   if(['HL', 'Corporate', 'SME', 'AIB'].includes($('#TLProduct').find(":selected").val())){
		$('#magicdiv1').removeClass('col-sm-12').addClass('col-sm-7')   ;
        $('#magicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
        $('#magicdiv4').show();
        if($('#TLProduct').find(":selected").val()=="HL"){
            $('#LTVGroup').show();
           // $('#RatingGroup').hide();
        } else {
            $('#LTVGroup').hide();
            //$('#RatingGroup').show();
        };
    } else{
        $('#magicdiv1').removeClass('col-sm-7').addClass('col-sm-12');
        $('#magicdiv2').removeClass('col-sm-5').addClass('col-sm-6');
        $('#magicdiv4').hide();
    };
	$('#other').change(function(){
		if( $(this).val()>0){
			$('#recurr').show();
		} else{
			$('#recurr').hide();
		}

	});
    $('#LTVGroup').hide();
	$('#recurr').hide();
	$('#LTVGroupODCC').hide();
	$('#recurrODCC').hide();
	$("#TLProduct").change(function(){
		if(['HL', 'Corporate', 'SME', 'AIB'].includes($(this).find(":selected").val())){
			$('#magicdiv1').removeClass('col-sm-12').addClass('col-sm-7');
			$('#magicdiv2').removeClass('col-sm-6').addClass('col-sm-5');
			$('#magicdiv4').show();
			if($(this).find(":selected").val()=="HL"){
				$('#LTVGroup').show();
				$('#RatingGroup').hide();
			} else {
				$('#LTVGroup').hide();
				$('#RatingGroup').show();
			};
		} else{
			$('#magicdiv1').removeClass('col-sm-7').addClass('col-sm-12');
			$('#magicdiv2').removeClass('col-sm-5').addClass('col-sm-6');
			$('#magicdiv4').hide();
		};
	});
	$('#other').change(function(){
		if( $(this).val()>0){
			$('#recurr').show();
		} else{
			$('#recurr').hide();
		}
		
	});
	$("#ODCCProduct").change(function(){
		if(['HL', 'Corporate', 'SME', 'AIB'].includes($(this).find(":selected").val())){
			$('#magicdiv1ODCC').removeClass('col-sm-12').addClass('col-sm-7');
			$('#magicdiv2ODCC').removeClass('col-sm-6').addClass('col-sm-5');
			$('#magicdiv4ODCC').show();
			if($(this).find(":selected").val()=="HL"){
				$('#LTVGroupODCC').show();
				$('#RatingGroupODCC').hide();
			} else {
				$('#LTVGroupODCC').hide();
				$('#RatingGroupODCC').show();
			};
		} else{
			$('#magicdiv1ODCC').removeClass('col-sm-7').addClass('col-sm-12');
			$('#magicdiv2ODCC').removeClass('col-sm-5').addClass('col-sm-6');
			$('#magicdiv4ODCC').hide();
		};
	});
	$('#otherODCC').change(function(){
		if( $(this).val()>0){
			$('#recurrODCC').show();
		} else{
			$('#recurrODCC').hide();
		}
		
	});
	if(['HL', 'Corporate', 'SME', 'AIB'].includes($('#ODCCProduct').find(":selected").val())){
        $('#magicdiv1ODCC').removeClass('col-sm-12').addClass('col-sm-7');
        $('#magicdiv2ODCC').removeClass('col-sm-6').addClass('col-sm-5');
        $('#magicdiv4ODCC').show();
        if($('ODCCProduct').find(":selected").val()=="HL"){
            $('#LTVGroupODCC').show();
            $('#RatingGroupODCC').hide();
        } else {
            $('#LTVGroupODCC').hide();
            $('#RatingGroupODCC').show();
        };
    } else{
        $('#magicdiv1ODCC').removeClass('col-sm-7').addClass('col-sm-12');
        $('#magicdiv2ODCC').removeClass('col-sm-5').addClass('col-sm-6');
        $('#magicdiv4ODCC').hide();
    };
});
