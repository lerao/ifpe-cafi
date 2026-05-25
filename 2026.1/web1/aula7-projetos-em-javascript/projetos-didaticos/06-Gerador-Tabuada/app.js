/**
 * Projeto: Gerador de Tabuada
 * Objetivo: Ensinar laços de repetição (for) e construção dinâmica de listas.
 */

const inputNumero = document.getElementById('numero');
const botaoGerar = document.getElementById('btnGerar');
const listaTabuada = document.getElementById('listaTabuada');

function gerarTabuada() {
    const num = Number(inputNumero.value);

    // 1. Limpamos a lista antes de gerar uma nova
    listaTabuada.innerHTML = "";

    // 2. Iniciamos o laço de repetição (loop)
    // O loop começa em 1 e vai até 10
    for (let i = 1; i <= 10; i++) {
        const resultado = num * i;

        // Criamos o texto da linha
        const textoLinha = `${num} x ${i} = ${resultado}`;

        // Criamos um novo elemento de lista (LI) usando template string
        // E adicionamos classes do Bootstrap
        listaTabuada.innerHTML += `<li class="list-group-item">${textoLinha}</li>`;
    }
}

botaoGerar.addEventListener('click', gerarTabuada);
