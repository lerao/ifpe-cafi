<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];

    if ($usuario === 'admin' && $senha === 'admin123') {
        $_SESSION['logado'] = true;
        $_SESSION['usuario'] = $usuario;
        header('Location: index.php');
        exit;
    } else {
        $_SESSION['erro_login'] = 'Usuário ou senha inválidos';
        header('Location: index.php');
        exit;
    }
}

header('Location: index.php');
exit;