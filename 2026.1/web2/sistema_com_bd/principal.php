<?php
include_once 'validasessao.php';
require_once 'classes.php';
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Principal - Sistema Bancário</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class="bg-light">
    <?php include 'menu.php'; ?>
    <main class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-10 col-lg-8">
                <div class="card shadow-sm border-0">
                    <div class="card-body p-4">
                        <h1 class="h3 mb-3">Realizar Transação</h1>
                        
                        <?php
                        $saldo = ContaCorrente::getSaldoAtual($pdo, $_SESSION['usuario_id']);
                        ?>
                        <div class="alert alert-info mb-4">
                            <strong>Saldo Atual:</strong> R$ <?= number_format($saldo, 2, ',', '.') ?>
                        </div>

                        <?php if (isset($_GET['msg'])): ?>
                            <div class="alert alert-warning" role="alert">
                                <?= htmlspecialchars($_GET['msg']) ?>
                            </div>
                        <?php endif; ?>

                        <p class="text-muted mb-4">Escolha o tipo de operação e informe o valor desejado.</p>
                        
                        <form action="processa_transacao.php" method="post" class="row g-3">
                            <div class="col-12 col-md-6">
                                <label for="valor" class="form-label">Valor (R$)</label>
                                <input type="number" id="valor" name="valor" class="form-control form-control-lg" step="0.01" min="0.01" placeholder="0,00" required autofocus>
                            </div>
                            <div class="col-12 col-md-6 d-flex align-items-end">
                                <div class="d-grid gap-2 w-100">
                                    <button type="submit" name="tipo" value="Deposito" class="btn btn-success btn-lg">Depositar</button>
                                    <button type="submit" name="tipo" value="Saque" class="btn btn-warning btn-lg">Sacar</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
