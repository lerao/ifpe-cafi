/**
 * Projeto: Calculadora de Desconto
 * Objetivo: Ensinar cálculos de porcentagem e formatação monetária.
 */

const inputValorOriginal = document.getElementById('valorOriginal');
const inputPorcentagem = document.getElementById('porcentagemDesconto');
const botaoCalcular = document.getElementById('btnCalcular');
const divResultado = document.getElementById('resultado');

function calcularDesconto() {
    const valor = Number(inputValorOriginal.value);
    const descontoPorcento = Number(inputPorcentagem.value);

    // Cálculo do valor a ser subtraído
    const valorDesconto = valor * (descontoPorcento / 100);
    
    // Cálculo do preço final
    const precoFinal = valor - valorDesconto;

    // Exibição do resultado
    // Usamos toLocaleString para formatar como moeda brasileira (R$)
    divResultado.innerHTML = `
        <p class="mb-1 text-muted">Valor do desconto: R$ ${valorDesconto.toFixed(2)}</p>
        <p class="mb-0">Preço com Desconto: R$ ${precoFinal.toFixed(2)}</p>
    `;
}

botaoCalcular.addEventListener('click', calcularDesconto);
