<?php
//2ª Questão -Faça um for (padrão) que calcule a soma dos 100 primeiros números
//(do 0 ao 100).
$soma = 0;
for ($i = 0; $i <= 100; $i++) {
    $soma = $soma + $i;
}   
echo "A soma dos 100 primeiros números é: " . $soma;
?>