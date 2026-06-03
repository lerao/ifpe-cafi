<?php
require_once 'validasessao.php';
require_once 'conexao.php';
require_once 'classes.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $tipo = $_POST['tipo'];
    $valor = (float) $_POST['valor'];
    $usuario_id = $_SESSION['usuario_id'];

    $conta = new ContaCorrente();
    
    $sucesso = false;
    if ($tipo == 'Deposito') {
        $sucesso = $conta->depositar($pdo, $usuario_id, $valor);
    } elseif ($tipo == 'Saque') {
        // Opcional: validar saldo aqui antes de sacar
        $saldoAtual = ContaCorrente::getSaldoAtual($pdo, $usuario_id);
        if ($saldoAtual >= $valor) {
            $sucesso = $conta->sacar($pdo, $usuario_id, $valor);
        } else {
            header('Location: principal.php?msg=Saldo insuficiente.');
            exit();
        }
    }

    if ($sucesso) {
        header('Location: historico.php');
    } else {
        echo "Erro ao realizar transação.";
    }
}
