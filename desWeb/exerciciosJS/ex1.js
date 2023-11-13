function calcularAumento() {
    let salario = parseFloat(document.getElementById("salario").value);
    let percentual = parseFloat(document.getElementById("percentual").value);

    let aumento = (salario * percentual) / 100;
    let novoSalario = salario + aumento;

    document.getElementById("resultado").innerText = (`Seu salário com aumento será R$ ${novoSalario}.`);
}