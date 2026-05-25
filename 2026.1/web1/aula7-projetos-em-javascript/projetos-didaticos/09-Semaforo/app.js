/**
 * Projeto: Semáforo Inteligente
 * Objetivo: Ensinar automação com timers (setInterval) e uso de arrays.
 */

const img = document.getElementById('imgSemaforo');
const botoes = document.querySelector('.d-flex');
const statusBadge = document.getElementById('status');

let intervaloId = null;
let indiceCor = 0;

// Objeto que mapeia o ID do botão para o caminho da imagem
const cores = {
    'vermelho': 'img/vermelho.png',
    'amarelo': 'img/amarelo.png',
    'verde': 'img/verde.png'
};

function mudarCor(idCor) {
    pararAutomatico(); // Para o modo automático se o usuário clicar manual
    img.src = cores[idCor];
    statusBadge.textContent = "Modo: Manual";
}

function alternarCor() {
    // Lista de cores para o modo automático
    const listaCores = ['vermelho', 'amarelo', 'verde'];
    const corAtual = listaCores[indiceCor];
    
    img.src = cores[corAtual];

    // Lógica para rodar o índice (0, 1, 2 e volta para 0)
    indiceCor = indiceCor < 2 ? ++indiceCor : 0;
}

function iniciarAutomatico() {
    pararAutomatico(); // Garante que não existam dois timers rodando ao mesmo tempo
    statusBadge.textContent = "Modo: Automático";
    statusBadge.className = "badge bg-primary p-2 fs-6";
    
    // Inicia o timer para mudar a cor a cada 1 segundo (1000ms)
    intervaloId = setInterval(alternarCor, 1000);
}

function pararAutomatico() {
    clearInterval(intervaloId);
    intervaloId = null;
    statusBadge.className = "badge bg-secondary p-2 fs-6";
}

// Delegação de Eventos: Escutamos cliques no container de botões
botoes.addEventListener('click', (event) => {
    const id = event.target.id;
    
    if (id === 'automatico') {
        iniciarAutomatico();
    } else if (cores[id]) {
        mudarCor(id);
    }
});
