/**
 * Projeto: Teste de Aptidão Física
 * Objetivo: Ensinar operadores relacionais e lógica de aprovação.
 */

const inputTempo = document.getElementById('tempo');
const botaoAvaliar = document.getElementById('btnAvaliar');
const divResultado = document.getElementById('resultado');

// Tempo limite para aprovação
const TEMPO_LIMITE = 15;

function avaliarAptidao() {
    const tempoCandidato = Number(inputTempo.value);

    // Verificação de segurança
    if (tempoCandidato <= 0) {
        divResultado.innerHTML = "Insira um tempo válido!";
        return;
    }

    // Lógica principal: No atletismo, quanto MENOR o tempo, melhor.
    // Usamos o operador <= (menor ou igual)
    if (tempoCandidato <= TEMPO_LIMITE) {
        divResultado.innerHTML = `<span class="text-success">APROVADO! 🎉</span>`;
    } else {
        divResultado.innerHTML = `<span class="text-danger">REPROVADO. ❌</span>`;
    }
}

botaoAvaliar.addEventListener('click', avaliarAptidao);
