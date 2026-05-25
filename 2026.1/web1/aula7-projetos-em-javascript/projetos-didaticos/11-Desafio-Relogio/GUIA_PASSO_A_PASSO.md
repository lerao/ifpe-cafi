# Desafio Guiado: Criando seu Relógio com Alarme ⏰

Neste desafio, você vai construir um relógio digital que atualiza em tempo real e permite configurar um alarme sonoro. Siga os passos abaixo, copiando o código para o seu arquivo `app.js` e observando a mágica acontecer!

---

## Passo 1: Fazer o relógio aparecer!
Atualmente o relógio está parado em `00:00:00`. Vamos capturar o elemento da tela e criar uma função para pegar a hora atual do computador.

**Copie e cole no seu `app.js`:**
```javascript
const displayRelogio = document.getElementById('relogio');

function atualizarRelogio() {
    // Pegamos a data e hora atual
    const agora = new Date();
    
    // Extraímos horas, minutos e segundos
    // Usamos padStart(2, '0') para garantir que sempre tenha 2 dígitos (ex: 09 em vez de 9)
    const horas = String(agora.getHours()).padStart(2, '0');
    const minutos = String(agora.getMinutes()).padStart(2, '0');
    const segundos = String(agora.getSeconds()).padStart(2, '0');

    // Montamos o texto
    const horaFormatada = `${horas}:${minutos}:${segundos}`;

    // Colocamos na tela
    displayRelogio.textContent = horaFormatada;
}

// Chamamos uma vez para não começar zerado
atualizarRelogio();
```
*Salve o arquivo e veja que a hora apareceu, mas ela ainda não "anda".*

---

## Passo 2: Fazer o relógio "viver" (Tick-Tack)
Para o relógio atualizar todo segundo, precisamos do `setInterval`.

**Adicione isso ao final do seu `app.js`:**
```javascript
// Executa a função atualizarRelogio a cada 1000 milissegundos (1 segundo)
setInterval(atualizarRelogio, 1000);
```
*Agora seu relógio deve estar contando os segundos em tempo real!*

---

## Passo 3: Preparar o sistema de Alarme
Agora vamos capturar os novos elementos: o input de tempo, o botão e o som.

**Adicione estas variáveis no TOPO do seu `app.js`:**
```javascript
const inputAlarme = document.getElementById('inputAlarme');
const btnDefinir = document.getElementById('btnDefinir');
const statusAlarme = document.getElementById('statusAlarme');
const somAlarme = document.getElementById('somAlarme');

let horaAlarme = null; // Guardará a hora que o usuário escolher
```

---

## Passo 4: Definir a hora do Alarme
Precisamos de uma função que guarde a hora que o aluno digitar no campo.

**Adicione esta função e o evento ao final do seu `app.js`:**
```javascript
function definirAlarme() {
    horaAlarme = inputAlarme.value; // Pega o valor do tipo "HH:MM"
    
    if (horaAlarme) {
        statusAlarme.textContent = `Alarme definido para: ${horaAlarme}`;
        statusAlarme.className = "mt-2 small text-info";
    }
}

btnDefinir.addEventListener('click', definirAlarme);
```

---

## Passo 5: O Grande Final - Verificar o Alarme!
Precisamos que, a cada segundo, o JavaScript verifique: "A hora atual é igual à hora do alarme?".

**Modifique sua função `atualizarRelogio` para incluir a verificação (substitua a função antiga por esta):**
```javascript
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
    }
}
```

---

### 🎉 Parabéns!
Você acaba de criar um aplicativo funcional de Relógio com Alarme.
**Desafio Extra:** Você consegue adicionar um botão para "Parar Alarme" que limpa a variável `horaAlarme` e pausa o som?
