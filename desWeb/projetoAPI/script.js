elemento = document.getElementById('pesquisa')
                                    //async = espera o tempo resposta da API sem travar o site
elemento.addEventListener('click', async function(){
    document.getElementById('resultado').innerText = ""
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {                  // /\D deixa somente digitos, /g de forma global, substitui por '' espaço
        var cep = valor.replace(/\D/g, '');
                        // / pode ser qualquer digito de 0-9 e precisa ter 8 ^pra iniciar o regex e $ para finalizar
        var validacep = /^[0-9]{8}$/;
   
        if(validacep.test(cep)) {
        var api = `https://viacep.com.br/ws/${cep}/json/`;
                        // await aguarda o resultado para fazer a atribuição, fetch() faz uma requisição da api
        let resposta = await fetch(api);
                // aguarda e converte o json para um objeto no js
        dados = await resposta.json();
        console.log(dados);
        if (dados.erro)
           document.getElementById('resultado').innerText = "CEP Não Existe";
        else
           document.getElementById('resultado').innerText = `CEP: ${dados.cep}, Rua: ${dados.logradouro}, Bairro: ${dados.bairro}, Cidade: ${dados.localidade}, DDD: ${dados.ddd}, Estado: ${dados.uf}.`
        }
    }
})