// functions to update the total value when qt is changed


function update_total_value(id){
            // gets the value from the price and qt box
            preco = parseInt(document.getElementById(id).value)
            qtd = parseInt(document.getElementById('number'+id).value)

            // multiply and update price box
            var total = qtd * preco
            document.getElementById('total'+id).value = "R$"+ total
    } 
    
function add_to_qt(id){
        // gets the value from the qt box
        var qtd = parseInt(document.getElementById('number'+id).value)

        // increments qt and updates price box
        document.getElementById('number'+id).value = qtd + 1;
        update_total_value(id)
    }

function sub_from_qt(id){
        // gets the value from the qt box
        var qtd = parseInt(document.getElementById('number'+id).value)

        //if qt == 1 throws a warning and sets value back to 1
        if (qtd == 1) {
            window.alert("Warning");
            qtd = 1;
            update_total_value(id)
        } else {

            //decrements qtd and updates price box
            qtd = qtd - 1;
            document.getElementById('number'+id).value = qtd
            update_total_value(id)
        }
    }