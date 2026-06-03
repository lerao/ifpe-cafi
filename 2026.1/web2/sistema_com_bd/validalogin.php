<?php
session_start();
require_once 'conexao.php';

$usuario_input = $_POST['usuario'];
$senha_input = $_POST['senha'];

// Consulta preparada para evitar SQL Injection
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE usuario = ?");
$stmt->execute([$usuario_input]);
$user = $stmt->fetch();

if ($user && $senha_input == $user['senha']) {
    $_SESSION['usuario_id'] = $user['id'];
    $_SESSION['usuario'] = $user['nome'];
    $_SESSION['logado'] = true;
    header('Location: principal.php');
    die();
} else {
    header('Location: index.php?msg=Login ou senha incorretos.');
    die();
}
?>