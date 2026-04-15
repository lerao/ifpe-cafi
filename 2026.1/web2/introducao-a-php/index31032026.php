<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 01/04</title>
</head>
<body>
    <!-- Senha Secreta -->
    <?php 
    // <?php ? > 
    // //é usado para comentários de uma única linha
    //Echo = print em php
    echo "IFPE" ?>
    Oi =D

    <br><br>
    <?php

    $nome = "Lairson";
    $idade = 20;
    //$idade = 20.4;
    //$idade = "Indefinida";
    //echo $nome;
    //echo $idade;

    echo "Meu nome é " . $nome . " e eu tenho " . $idade . " anos de idade<br>";
    echo "Meu nome é $nome e eu tenho $idade anos de idade";

    echo "<br>";
    if ($idade >= 20){
        echo "Você é maior de idade.";
    } else {
        echo "Você não é maior de idade.";
    }

    $a="4";
    if ($a==4) {
        echo "true";
    } else {
        echo "false";
    }
    echo $a==4;

    ?>

</body>
</html>