

  $(document).ready(function() {

	//code for adding and removing buttons based on tutorial from https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery 
	var max_fields      = 30; //maximum input boxes allowed
    var ing_wrapper   		= $(".input_ingredient_wrap"); 
    var dir_wrapper   		= $(".input_direction_wrap"); 
	var add_ingredient      = $(".add_ingredient_button"); //Add description ID
    var add_direction      = $(".add_direction_button"); //Add ingredent ID

	//add ingredient and amount text box on click 
	var x = 1; //initlal text box count
	$(add_ingredient).click(function(e){ 
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(ing_wrapper).append('<div class="row"><div class="col"><input type="text" id="ingredient" name="Ingredient" size="120"></div><div class="col"><input type="text" id="amount" name="Amount" size="15"></div><a href="#" id="remove" class="remove_field">Remove</a></div>'); //add input box
		}
	});

	//remove ingredient box and amount on click 
    $(ing_wrapper).on("click",".remove_field", function(e){ 
		e.preventDefault(); $(this).parent('div').remove();  x--;
	})

	//add description on click 
    var y = 1; //initlal text box count
	$(add_direction).click(function(e){ 
		e.preventDefault();
		if(y < max_fields){ //max input box allowed
			y++; //text box increment
			$(dir_wrapper).append('<div><input type="text" id="direction" name="Direction" size="150"><a href="#" id="remove" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	//remove description on click
	$(dir_wrapper).on("click",".remove_field", function(e){ 
		e.preventDefault(); $(this).parent('div').remove(); y--;
	})
});