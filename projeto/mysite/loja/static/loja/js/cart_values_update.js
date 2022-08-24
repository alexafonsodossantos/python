
function teste(){
    console.log("file is loaded");
}

function updateValue(id){
            // x = preco
            x = parseInt(document.getElementById(id).value)
            console.log(x)
    
            // value = qtd
            value = parseInt(document.getElementById('number'+id).value)
            console.log(value)
    
            var total = value * x
            document.getElementById('total'+id).value = "R$"+ total
    } 
    
function add(id){
        var v1 = parseInt(document.getElementById('number'+id).value)
        document.getElementById('number'+id).value = v1 + 1;
        updateValue(id)
    }

function sub(id){
        var v1 = parseInt(document.getElementById('number'+id).value)
        if (v1 == 1) {
            window.alert("ayyyyy");
            v1 = 1;
            updateValue(id)
        } else {
            v1 = v1 - 1;
            document.getElementById('number'+id).value = v1
            updateValue(id)
        }
    }

