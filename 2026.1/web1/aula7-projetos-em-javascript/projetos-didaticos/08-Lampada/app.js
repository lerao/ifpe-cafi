/**
 * Projeto: Lâmpada Interativa
 * Objetivo: Ensinar manipulação de atributos de imagem e eventos de mouse variados.
 */

const lamp = document.getElementById('lamp');
const btnLigar = document.getElementById('btnLigar');
const btnDesligar = document.getElementById('btnDesligar');

// Função auxiliar para verificar se a lâmpada está quebrada
// Se o caminho da imagem contiver a palavra 'quebrada', retorna true
function estaQuebrada() {
    return lamp.src.indexOf('quebrada') > -1;
}

function ligarLampada() {
    if (!estaQuebrada()) {
        lamp.src = "img/ligada.jpg";
    }
}

function desligarLampada() {
    if (!estaQuebrada()) {
        lamp.src = "img/desligada.jpg";
    }
}

function quebrarLampada() {
    lamp.src = "img/quebrada.jpg";
}

// 1. Eventos de Clique nos Botões
btnLigar.addEventListener('click', ligarLampada);
btnDesligar.addEventListener('click', desligarLampada);

// 2. Eventos de Mouse (Passar e Tirar o mouse)
lamp.addEventListener('mouseover', ligarLampada);
lamp.addEventListener('mouseleave', desligarLampada);

// 3. Evento de Clique Duplo (Double Click)
lamp.addEventListener('dblclick', quebrarLampada);
