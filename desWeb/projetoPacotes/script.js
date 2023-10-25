let valorPacote = 0;
let adicionais = 0;
let totalAdicionais;

function calcularTotalViagem(){
   calcularPacote();
   calcularAdicionais();
}

function calcularAdicionais(){
    totalAdicionais = 0;
    let adicionais = document.querySelectorAll("input[name='adicionais']");
    console.log(adicionais);
    for(let i=0; i < adicionais.length; i++){
        if(adicionais[i].checked == true){
            totalAdicionais = totalAdicionais + parseFloat(adicionais[i].value);
        }
    }
    alert(`Adicionais: ${totalAdicionais}`);

}

function calcularPacote(){
    let qtdPacotes = document.querySelectorAll("input[name='pacotes']").length;
    console.log(qtdPacotes);

    let pacotes = document.querySelectorAll("input[name='pacotes']");
    
    console.log(pacotes);
    //         i < pacotes.length
    for(var i=0; i < qtdPacotes; i++)
    {
        if( pacotes[i].checked == true )
        {
            console.log(pacotes[i].value);
            valorPacote = pacotes[i].value;
            break;
        }
    }
}