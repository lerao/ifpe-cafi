<?php
//1ª Questão - Cálculo do fatorial de forma recursiva e iterativa
function calcularFatorialRecursivo($numero) {
    if ($numero == 1) {
        return 1;
    }
    return $numero * calcularFatorialRecursivo($numero-1);
}
echo "O fatorial de 5 é: " . calcularFatorialRecursivo(5); 

function calcularFatorial($numero) {
    $resultado = 1;

    // Multiplicamos o resultado por cada número de 1 até o valor desejado
    for ($i = 1; $i <= $numero; $i++) {
        $resultado = $resultado * $i;
    }

    return $resultado;
}
echo "O fatorial de 5 é: " . calcularFatorial(5); 
?>