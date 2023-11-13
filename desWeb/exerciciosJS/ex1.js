function calcularAumento() {
    // Obtém os valores informados pelo usuário
    let salario = parseFloat(document.getElementById("salario").value);
    let percentual = parseFloat(document.getElementById("percentual").value);

    // Calcula o novo salário com base no aumento percentual
    let aumento = (salario * percentual) / 100;
    let novoSalario = salario + aumento;

    // Exibe o resultado na página
    document.getElementById("resultado").innerText = (`Seu salário com aumento será R$ ${novoSalario}.`);
}