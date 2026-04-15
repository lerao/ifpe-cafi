<?php
$nascimento = 1990;
$ano = 2020; 

function calcularIdade() {
    $GLOBALS['idade'] = $GLOBALS['ano'] - $GLOBALS['nascimento'];
}

function calcularIdadeSemGlobal($ano, $nasc) {
    $idade = $ano - $nasc;
}

calcularIdade();
echo $idade;
?>