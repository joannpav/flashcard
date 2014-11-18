            if(!window.Kolich){
				Kolich = {};
			}
			
			Kolich.Selector = {};
			// getSelected() was borrowed from CodeToad at
			// http://www.codetoad.com/javascript_get_selected_text.asp
			Kolich.Selector.getSelected = function(){
				var t = '';
				if(window.getSelection){
					t = window.getSelection();
				}else if(document.getSelection){
					t = document.getSelection();
				}else if(document.selection){
					t = document.selection.createRange().text;
				}
				return t;
			}
			
			Kolich.Selector.mouseup = function(){
				var st = Kolich.Selector.getSelected();
				if((st!='') && ( $("#q").text() == ""))
                {
                    $("#q").append($('#list option:selected').text() + " " + $('#list2 option:selected').text()  + " " + st);
				}else if ( $("#a").text() == "") 
                {

                     $("#a").append(" " + st);
                }
			}

            /*$("#clearCard").click(function() {
                    $("#q").val("");
                    $("#a").val("");
            })*/


			$(document).ready(function(){
				$(document).bind("mouseup", Kolich.Selector.mouseup);
			});


             function ClearCard(){
                $("#q").empty().append(" ");
                $("#a").empty().append(" ");
                 

            }
            /*
                $("#clearCard").click(function() {
                    $("#q").val("");
                    $("#a").val("");
            });*/
