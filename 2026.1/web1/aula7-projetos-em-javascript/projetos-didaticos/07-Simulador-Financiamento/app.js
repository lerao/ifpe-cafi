/**
 * Projeto: Simulador de Financiamento
 * Objetivo: Ensinar cálculos financeiros básicos e manipulação de visibilidade (display).
 */

const inputValor = document.getElementById('valorTotal');
const inputEntrada = document.getElementById('entrada');
const inputJuros = document.getElementById('taxaJuros');
const inputParcelas = document.getElementById('parcelas');
const botaoSimular = document.getElementById('btnSimular');
const divResultado = document.getElementById('resultado');

function simular() {
    // 1. Coleta de dados
    const valorTotal = Number(inputValor.value);
    const entrada = Number(inputEntrada.value);
    const taxaJuros = Number(inputJuros.value) / 100; // Converte % para decimal
    const parcelas = Number(inputParcelas.value);

    // 2. Cálculos básicos
    const valorFinanciado = valorTotal - entrada;
    
    // Fórmula de Juros Simples para fins didáticos (Valor * (1 + (Juros * Tempo)))
    // Nota: Em financiamentos reais usa-se a Tabela Price, mas aqui focamos na lógica JS
    const valorComJuros = valorFinanciado * (1 + (taxaJuros * parcelas));
    const valorParcela = valorComJuros / parcelas;

    // 3. Exibição dos resultados
    // Mostramos a div de resultado removendo a classe 'd-none' do Bootstrap
    divResultado.classList.remove('d-none');

    divResultado.innerHTML = `
        <h4 class="text-primary mb-3">Resultado da Simulação</h4>
        <p>Valor Financiado: <strong>R$ ${valorFinanciado.toFixed(2)}</strong></p>
        <p>Total a pagar com Juros: <strong>R$ ${valorComJuros.toFixed(2)}</strong></p>
        <hr>
        <h5>Valor da Parcela:</h5>
        <h2 class="text-success">R$ ${valorParcela.toFixed(2)}</h2>
        <small class="text-muted">Simulação baseada em juros simples.</small>
    `;
}

botaoSimular.addEventListener('click', simular);
