<?php

#Descrevendo uma pessoa
$dados = array("Fulano", 36, "Afogados");
$dados_com_chave = array("nome" => "Fulano", 
                        "idade" => 36, 
                        "cidade" => "Afogados");

print_r($dados);
echo "<hr />";
print_r($dados_com_chave);

?>