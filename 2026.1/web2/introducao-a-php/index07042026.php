<?php
$a = array();
$a[0] = 87;
$b = array("A", 5, 3.4);
var_dump($a);
echo "<br>";
var_dump($b);

function somar($a , $b){
      return  $a+$b;
}
function imprimirNomeCompleto ($nome,$Sobrenome)
{
      echo $nome.' '.$Sobrenome;
}


echo(somar(5, 10));
echo "<br>";
imprimirNomeCompleto("João", "Silva");


$a = 4 + 5; //int + int
$b = "4" + 2; // String + int
$c = "5" + "-2"; // String + String;
$d = "5" . "-2"; // String . String;
$e = 3 + "2 patinhos na lagoa"; // int + String;
$f = 3 . "2 patinhos na lagoa"; // int . String;
echo "a: $a <br>";
echo "b: $b <br>";
echo "c: $c <br>";
echo "d: $d <br>";
echo "e: $e <br>";
echo "f: $f <br>";

//Foco nos operadores
//Operador matemático (+)) : O PHP tentará converter tudo em número.
//Operador de string (.): O PHP tentará converter tudo em texto (String).   


//Evite fazer essas somas sem saber o que está acontecendo, pois pode gerar resultados inesperados. 
// Sempre verifique os tipos de dados envolvidos nas operações para evitar confusões.
?>
