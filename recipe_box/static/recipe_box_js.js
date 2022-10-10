

  $(document).ready(function() {
	var max_fields      = 30; //maximum input boxes allowed
    var ing_wrapper   		= $(".input_ingredient_wrap"); //Fields wrapper
    var dir_wrapper   		= $(".input_direction_wrap"); //Fields wrapper
	var add_ingredient      = $(".add_ingredient_button"); //Add button ID
    var add_direction      = $(".add_direction_button"); //Add button ID

	
	var x = 1; //initlal text box count
	$(add_ingredient).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(ing_wrapper).append('<div class="row"><div class="col"><input type="text" id="Ingredient" name="Ingredient" size="120"><a href="#" class="remove_field">Remove</a></div><div class="col"><input type="text" id="Amount" name="Amount" size="15"><a href="#" class="remove_field">Remove</a></div></div>'); //add input box
		}
	});

    $(ing_wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove();  x--;
	})

    var y = 1; //initlal text box count
	$(add_direction).click(function(e){ //on add input button click
		e.preventDefault();
		if(y < max_fields){ //max input box allowed
			y++; //text box increment
			$(dir_wrapper).append('<div><input type="text" id="Direction" name="Direction" size="150"><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(dir_wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); y--;
	})
});