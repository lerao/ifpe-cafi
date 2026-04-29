<?php
session_start();

if (!isset($_SESSION['usuario']) || empty($_SESSION['usuario'])) {
    header('Location: login.php');
    exit;
}

$usuario = $_SESSION['usuario'];
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Página Principal</title>
</head>
<body>
    <h1>Bem-vindo, <?php echo htmlspecialchars($usuario, ENT_QUOTES, 'UTF-8'); ?>!</h1>
    <p>Você está logado e pode acessar esta página.</p>
    <p><a href="logout.php">Sair</a></p>
</body>
</html>