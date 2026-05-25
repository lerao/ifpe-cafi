/**
 * Projeto: Contador Digital
 * Objetivo: Ensinar escopo de variáveis e manipulação múltipla de DOM.
 */

// 1. Iniciamos uma variável global para guardar o valor atual
let contador = 0;

// 2. Capturamos os elementos
const divValor = document.getElementById('valor');
const botaoDiminuir = document.getElementById('btnDiminuir');
const botaoReset = document.getElementById('btnReset');
const botaoAumentar = document.getElementById('btnAumentar');

// 3. Função para atualizar a tela e a cor
function atualizarTela() {
    divValor.textContent = contador;

    // Lógica de cores baseada no valor
    if (contador > 0) {
        divValor.style.color = "green";
    } else if (contador < 0) {
        divValor.style.color = "red";
    } else {
        divValor.style.color = "black";
    }
}

// 4. Funções de ação
function aumentar() {
    contador = contador + 1; // ou contador++
    atualizarTela();
}

function diminuir() {
    contador = contador - 1; // ou contador--
    atualizarTela();
}

function resetar() {
    contador = 0;
    atualizarTela();
}

// 5. Atribuindo os eventos
botaoAumentar.addEventListener('click', aumentar);
botaoDiminuir.addEventListener('click', diminuir);
botaoReset.addEventListener('click', resetar);
