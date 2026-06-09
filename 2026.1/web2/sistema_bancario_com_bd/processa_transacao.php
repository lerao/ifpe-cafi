<?php
require_once 'validasessao.php';
require_once 'conexao.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $tipo = $_POST['tipo'];
    $valor = $_POST['valor'];
    $usuario_id = $_SESSION['usuario_id'];

    $stmt = $pdo->prepare("INSERT INTO transacoes (usuario_id, tipo, valor) VALUES (?, ?, ?)");
    
    if ($stmt->execute([$usuario_id, $tipo, $valor])) {
        header('Location: historico.php');
    } else {
        echo "Erro ao realizar transação.";
    }
}
?>