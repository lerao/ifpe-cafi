<?php
require_once 'classes.php';
$auth = new Auth();
$auth->requireLogin();
$user = $auth->currentUser();

// Inicializar conta na sessão se não existir
if (!isset($_SESSION['conta'])) {
    $conta = new ContaCorrente();
    $_SESSION['conta'] = $conta->toArray();
}
$conta = new ContaCorrente();
$conta = $conta->fromArray($_SESSION['conta']);

// Processar ações
$mensagem = '';
$extratoHtml = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $valor = filter_input(INPUT_POST, 'valor', FILTER_VALIDATE_FLOAT);
    $acao = filter_input(INPUT_POST, 'acao', FILTER_SANITIZE_SPECIAL_CHARS);

    if ($valor !== false && $valor > 0) {
        if ($acao === 'depositar') {
            $conta->depositar($valor);
            $mensagem = "Depósito de R$ " . number_format($valor, 2, ',', '.') . " realizado com sucesso.";
        } elseif ($acao === 'sacar') {
            if ($conta->getSaldo() >= $valor) {
                $conta->sacar($valor);
                $mensagem = "Saque de R$ " . number_format($valor, 2, ',', '.') . " realizado com sucesso.";
            } else {
                $mensagem = "Saldo insuficiente para saque.";
            }
        }
    } elseif ($acao === 'extrato') {
        $operacoes = $conta->gerarExtrato();
        if (!empty($operacoes)) {
            $extratoHtml = '<div class="card mt-3"><div class="card-body"><h2 class="h5 mb-3">Extrato de Operações</h2><div class="table-responsive"><table class="table table-sm mb-0"><thead><tr><th>Data</th><th>Tipo</th><th class="text-end">Valor</th></tr></thead><tbody>';

            foreach ($operacoes as $operacao) {
                $extratoHtml .= '<tr>';
                $extratoHtml .= '<td>' . htmlspecialchars($operacao['data']) . '</td>';
                $extratoHtml .= '<td>' . htmlspecialchars($operacao['tipo']) . '</td>';
                $extratoHtml .= '<td class="text-end">R$ ' . number_format($operacao['valor'], 2, ',', '.') . '</td>';
                $extratoHtml .= '</tr>';
            }

            $extratoHtml .= '</tbody></table></div></div></div>';
        } else {
            $mensagem = "Nenhuma operação realizada para gerar extrato.";
        }
    } else {
        $mensagem = "Valor inválido.";
    }

    // Salvar conta na sessão
    $_SESSION['conta'] = $conta->toArray();
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Conta Corrente</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class="bg-light">
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="principal.php">Conta Corrente</a>
        <div class="d-flex">
            <span class="navbar-text text-white me-3">Olá, <?= htmlspecialchars($user ?? 'Usuário') ?></span>
            <a class="btn btn-outline-light btn-sm" href="sair.php">Sair</a>
        </div>
    </div>
</nav>
<main class="container py-5">
    <div class="row justify-content-center">
        <div class="col-12 col-md-10 col-lg-8">
            <div class="card shadow-sm">
                <div class="card-body p-4">
                    <h1 class="h3 mb-3">Sua Conta Corrente</h1>
                    <div class="alert alert-info">
                        <strong>Saldo Atual:</strong> R$ <?= number_format($conta->getSaldo(), 2, ',', '.') ?>
                    </div>
                    <?php if ($mensagem): ?>
                        <div class="alert alert-success" role="alert">
                            <?= htmlspecialchars($mensagem) ?>
                        </div>
                    <?php endif; ?>
                    <?= $extratoHtml ?>
                    <form action="principal.php" method="post" class="row g-3">
                        <div class="col-12 col-md-6">
                            <label for="valor" class="form-label">Valor</label>
                            <input type="number" id="valor" name="valor" class="form-control" step="0.01" min="0.01" placeholder="0,00">
                        </div>
                        <div class="col-12 col-md-6 d-flex align-items-end">
                            <div class="d-grid gap-2 w-100">
                                <button type="submit" name="acao" value="depositar" class="btn btn-success">Depositar</button>
                                <button type="submit" name="acao" value="sacar" class="btn btn-warning">Sacar</button>
                            </div>
                        </div>
                        <div class="col-12">
                            <button type="submit" name="acao" value="extrato" class="btn btn-info w-100">Gerar Extrato</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</main>
</body>
</html>
