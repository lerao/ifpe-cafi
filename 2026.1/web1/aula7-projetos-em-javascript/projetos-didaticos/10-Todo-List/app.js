/**
 * Projeto: Lista de Tarefas (Todo-List)
 * Objetivo: Ensinar criação e remoção dinâmica de elementos HTML via JavaScript.
 */

const inputTarefa = document.getElementById('inputTarefa');
const btnAdicionar = document.getElementById('btnAdicionar');
const listaTarefas = document.getElementById('listaTarefas');

function adicionarTarefa() {
    const textoTarefa = inputTarefa.value.trim();

    // Validação: não adiciona tarefas vazias
    if (textoTarefa === "") {
        alert("Digite algo para fazer!");
        return;
    }

    // 1. Criamos o elemento de lista (LI)
    const li = document.createElement('li');
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    
    // 2. Definimos o conteúdo do LI
    li.innerHTML = `
        <span class="texto-item">${textoTarefa}</span>
        <button class="btn btn-danger btn-sm btn-excluir">
            <i class="bi bi-trash"></i>
        </button>
    `;

    // 3. Adicionamos o LI na nossa lista UL
    listaTarefas.appendChild(li);

    // 4. Limpamos o input e voltamos o foco para ele
    inputTarefa.value = "";
    inputTarefa.focus();

    // 5. Adicionamos os eventos de interação dentro da própria tarefa criada
    
    // Clique no texto para marcar como concluída (toggle class)
    const spanTexto = li.querySelector('.texto-item');
    spanTexto.addEventListener('click', () => {
        spanTexto.classList.toggle('concluida');
    });

    // Clique no botão de excluir para remover o item da lista
    const btnExcluir = li.querySelector('.btn-excluir');
    btnExcluir.addEventListener('click', () => {
        listaTarefas.removeChild(li);
    });
}

// Escuta o clique no botão
btnAdicionar.addEventListener('click', adicionarTarefa);

// Permite adicionar tarefa ao apertar a tecla 'Enter'
inputTarefa.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        adicionarTarefa();
    }
});
