/**
 * Projeto: Calculadora de IMC
 * Objetivo: Ensinar condicionais encadeadas (else if) e manipulação de DOM.
 */

const inputPeso = document.getElementById('peso');
const inputAltura = document.getElementById('altura');
const botaoCalcular = document.getElementById('btnCalcular');
const divResultado = document.getElementById('resultado');

function calcularIMC() {
    const peso = Number(inputPeso.value);
    const altura = Number(inputAltura.value);

    // Validação simples: se peso ou altura forem zero ou vazios
    if (peso <= 0 || altura <= 0) {
        divResultado.innerHTML = `<span class="text-danger">Por favor, insira valores válidos!</span>`;
        return; // Sai da função
    }

    // Fórmula: peso dividido por altura ao quadrado
    const imc = peso / (altura * altura);
    let classificacao = "";

    // Condicionais encadeadas para classificar o IMC
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
    } else if (imc < 25) {
        classificacao = "Peso normal (Parabéns!)";
    } else if (imc < 30) {
        classificacao = "Sobrepeso";
    } else if (imc < 35) {
        classificacao = "Obesidade Grau I";
    } else {
        classificacao = "Obesidade Grau II ou III";
    }

    // Exibindo o resultado formatado
    divResultado.innerHTML = `
        <div class="alert alert-info">
            Seu IMC é <strong>${imc.toFixed(2)}</strong><br>
            Situação: <strong>${classificacao}</strong>
        </div>
    `;
}

botaoCalcular.addEventListener('click', calcularIMC);
