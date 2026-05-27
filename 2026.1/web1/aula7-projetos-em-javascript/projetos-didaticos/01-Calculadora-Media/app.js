/**
 * Projeto: Calculadora de Média
 * Objetivo: Ensinar variáveis, tipos numéricos e condicionais.
 */

// 1. Capturamos os elementos do HTML que vamos usar
const inputNota1 = document.getElementById('nota1');
const inputNota2 = document.getElementById('nota2');
const botaoCalcular = document.getElementById('btnCalcular');
const divResultado = document.getElementById('resultado');

// 2. Criamos a função que faz o cálculo
function calcularMedia() {
    // Pegamos os valores dos inputs e convertemos para número
    console.log(inputNota1.value);
    console.log(inputNota2.value);
    const nota1 = Number(inputNota1.value);
    const nota2 = Number(inputNota2.value);

    // Calculamos a média simples
    const media = (nota1 + nota2) / 2;

    // Criamos uma variável para guardar a mensagem de situação
    let situacao = "";
    let corMensagem = "";

    // Verificamos se a média é maior ou igual a 7
    if (media >= 7) {
        situacao = "Aprovado!";
        corMensagem = "text-success"; // Classe do Bootstrap para verde
    } else {
        situacao = "Reprovado.";
        corMensagem = "text-danger"; // Classe do Bootstrap para vermelho
    }

    // Exibimos o resultado na tela
    divResultado.innerHTML = `Sua média é ${media.toFixed(1)} <br> <span class="${corMensagem}">${situacao}</span>`;
}

// 3. Adicionamos o evento de clique ao botão
botaoCalcular.addEventListener('click', calcularMedia);
