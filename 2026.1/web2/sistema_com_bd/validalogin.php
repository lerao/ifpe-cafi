<?php
session_start();

$usuario = $_POST['usuario'];
$senha = $_POST['senha'];

if ($usuario == 'admin' && $senha == 'admin123') {
    $_SESSION['usuario'] = "Teste Usuário";
    $_SESSION['logado'] = true;
    header('Location: principal.php');
    die();
} else {
    header('Location: index.php?msg=Login ou senha incorretos.');
    die();
}


?>