<?php

$usuario = $_POST['usuario'];
$senha = $_POST['senha'];

echo($usuario . "-" . $senha);

if (($usuario === 'admin')
    && ($senha === 'admin123')) {
    header("Location: principal.php");
    die();
} else {
    header("Location: index.php?msg=Login e senha incorretos!");
    die(); 
}

?>