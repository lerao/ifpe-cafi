<?php
session_start();

if (!isset($_SESSION['logado'])) {
    header('Location: index.php?msg=Faça login para acessar a página principal.');
    die();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <main>
        <h1>Bem Vindo <?php echo $_SESSION['usuario']; ?></h1>
        <p>Você está logado com sucesso!</p>
        <a href="sair.php">Sair</a>    
    </main
    
</body>
</html>