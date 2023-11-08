let combo = 0;
let valorEntrega = 0;

function calcularTotal(){
    calcularCombo();
    calcularAdicional();
    calcularEntrega();
    let valorTotal = combo + totalAdicional + valorEntrega;
    document.getElementById('pagamento').value = (`O total a pagar é R$ ${valorTotal}.`)
    document.getElementById('descricao').innerText = (`Seu combo custará R$ ${combo} com R$ ${totalAdicional} de adicionais e R$ ${valorEntrega} de taxa de entrega.`)
}

function calcularCombo(){
    combo = Number(document.getElementById('combo').value);
    console.log(combo)
}

function calcularAdicional(){
    totalAdicional = 0;
    let adicional = document.querySelectorAll("input[name='adicional']");
    for(let i=0; i < adicional.length; i++){
        if(adicional[i].checked == true){
            totalAdicional += Number(adicional[i].value);
        }
    }
    console.log(totalAdicional)
}

function calcularEntrega(){
    let entrega = document.querySelectorAll("input[type='radio']");
    console.log
    for(let  i=0; i < entrega.length; i++){
        if(entrega[i].checked){
            valorEntrega = Number(entrega[i].value)
        }
    }
    console.log(valorEntrega)
    
}



