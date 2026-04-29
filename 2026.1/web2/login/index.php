<?php
session_start();
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Tela de Login</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        form { border: 1px solid #ccc; padding: 20px; border-radius: 5px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; margin-bottom: 10px; }
        button { padding: 10px; width: 100%; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <form action="validalogin.php" method="post">
        <h2>Login</h2>
        <label for="username">Usuário:</label>
        <input type="text" name="usuario" id="username" required>
        
        <label for="password">Senha:</label>
        <input type="password" name="senha" id="password" required>
        
        <button type="submit">Entrar</button>
    </form>
</body>
</html>