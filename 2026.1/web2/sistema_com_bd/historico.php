<?php
include_once 'validasessao.php';
require_once 'classes.php';
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Histórico - Sistema Bancário</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class="bg-light">
    <?php include 'menu.php'; ?>
    <main class="container">
        <div class="row justify-content-center">
            <div class="col-12 col-md-10 col-lg-8">
                <div class="card shadow-sm border-0">
                    <div class="card-body p-4">
                        <h1 class="h3 mb-3">Extrato de Operações</h1>
                        <p class="text-muted mb-4">Confira abaixo todas as movimentações realizadas em sua conta.</p>

                        <div class="table-responsive">
                            <table class="table table-hover mb-0">
                                <thead class="table-light">
                                    <tr>
                                        <th>Data</th>
                                        <th>Tipo</th>
                                        <th class="text-end">Valor</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php
                                    $conta = new ContaCorrente();
                                    $transacoes = $conta->getOperacoes($pdo, $_SESSION['usuario_id']);

                                    if (count($transacoes) > 0) {
                                        foreach ($transacoes as $t) {
                                            $isDeposito = ($t['tipo'] == 'Deposito');
                                            $classe = $isDeposito ? 'text-success' : 'text-danger';
                                            $sinal = $isDeposito ? '' : '- ';
                                            echo "<tr>";
                                            echo "<td>" . date('d/m/Y H:i', strtotime($t['data_hora'])) . "</td>";
                                            echo "<td class='$classe fw-bold'>" . htmlspecialchars($t['tipo']) . "</td>";
                                            echo "<td class='text-end $classe'>$sinal R$ " . number_format($t['valor'], 2, ',', '.') . "</td>";
                                            echo "</tr>";
                                        }
                                    } else {
                                        echo "<tr><td colspan='3' class='text-center text-muted py-4'>Nenhuma transação encontrada.</td></tr>";
                                    }
                                    ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
