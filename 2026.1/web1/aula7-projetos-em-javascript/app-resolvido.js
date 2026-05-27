// Este arquivo começará vazio para o estudante.
// O código será preenchido seguindo o GUIA_PASSO_A_PASSO.md

const displayRelogio = document.getElementById('relogio');
const inputAlarme = document.getElementById('inputAlarme');
const btnDefinir = document.getElementById('btnDefinir');
const statusAlarme = document.getElementById('statusAlarme');
const somAlarme = document.getElementById('somAlarme');
let horaAlarme = null; // Guardará a hora que o usuário escolher
let alarmeTocando = false; // Flag para controlar se o alarme já foi disparado


function atualizarRelogio() {
    const agora = new Date();
    const horas = String(agora.getHours()).padStart(2, '0');
    const minutos = String(agora.getMinutes()).padStart(2, '0');
    const segundos = String(agora.getSeconds()).padStart(2, '0');

    const horaFormatada = `${horas}:${minutos}:${segundos}`;
    displayRelogio.textContent = horaFormatada;

    // VERIFICAÇÃO DO ALARME
    // Comparamos apenas Horas:Minutos
    const horaMinutoAtual = `${horas}:${minutos}`;

    if (horaAlarme === horaMinutoAtual) {
        somAlarme.play(); // Toca o bip!
        statusAlarme.textContent = "ACORDA!!! 🔔";
        statusAlarme.className = "mt-2 small text-danger fw-bold";

        const btnPararAlarme = document.createElement('button');
        btnPararAlarme.textContent = "Parar Alarme";
        btnPararAlarme.className = "btn btn-sm btn-secondary mt-2";
        statusAlarme.appendChild(btnPararAlarme);

        btnPararAlarme.addEventListener('click', () => {
            somAlarme.pause();
            somAlarme.currentTime = 0;   
            statusAlarme.textContent = "Alarme parado.";
            statusAlarme.className = "mt-2 small text-info";
        });

    }
}

// Chamamos uma vez para não começar zerado
atualizarRelogio();

// Executa a função atualizarRelogio a cada 1000 milissegundos (1 segundo)
setInterval(atualizarRelogio, 1000);


function definirAlarme() {
    horaAlarme = inputAlarme.value; // Pega o valor do tipo "HH:MM"
    
    if (horaAlarme) {
        statusAlarme.textContent = `Alarme definido para: ${horaAlarme}`;
        statusAlarme.className = "mt-2 small text-info";
    }
}

btnDefinir.addEventListener('click', definirAlarme);

