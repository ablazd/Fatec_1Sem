elemento = document.getElementById("pesquisa");

x = document.getElementById('pesquisaClima')
x.addEventListener('click', async function ()
{
    cidade = document.getElementById('cidade').value;
    const apiClimaURL = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&units=metric&appid=${'apiKey'}&lang=pt_br`;
    let respostaClima = await fetch(apiClimaURL);
    let dadosClima = await respostaClima.json();
    temperatura = dadosClima.main.temp;
    descricao = dadosClima.weather[0].description;
    document.getElementById('resultadoClima').innerHTML = `Hoje está ${temperatura}${descricao}`
})

elemento.addEventListener('click', async function () {
    document.getElementById('resultado').innerText = ""
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {
        var cep = valor.replace(/\D/g, '');
        var validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var api = `https://viacep.com.br/ws/${cep}/json/`;

            let resposta = await fetch(api);
            let dados = await resposta.json();
            console.log(dados);
            if (dados.erro)
                document.getElementById('resultado').innerText = "CEP Não Existe";
            else
                document.getElementById('resultado').innerText = dados.logradouro + ", " + dados.bairro + " - " + dados.localidade + ", " + dados.uf
                document.getElementById('cidade').value = dados.localidade
        }
        else
            if (!(resposta.ok))
                alert("cep inválido");
    }
}
)