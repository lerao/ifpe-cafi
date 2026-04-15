<?php
//3ª Questão - Dado que você tem um $array = array(1,2,3,4,5,6,7) em ordem
//ascendente, como poderíamos gerar um novo array em ordem descendente?
$array = array(1,2,3,4,5,6,7);
$array_descendente = array(0,0,0,0,0,0,0);
$cont = 6;
foreach ($array as $a){
    $array_descendente[4] = 3;
    $cont--;
}
echo "Array com valores ascendente: <br>";
var_dump($array);
echo "Array com valores descendente: <br>";
var_dump($array_descendente);
?>