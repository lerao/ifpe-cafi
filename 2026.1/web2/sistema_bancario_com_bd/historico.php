<?php
include_once 'validasessao.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
    <main>
        <div class="container">
            <?php include 'menu.php'; ?>
            <div class="row">
                <div class="col-md-6 offset-md-3">
                    <h1><mark>Histórico</mark></h1>
                    <h1>Bem Vindo <?php echo $_SESSION['usuario']; ?></h1>
                    
                    <p>Veja abaixo seu histórico de transações:</p>

                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Data</th>
                                <th>Tipo</th>
                                <th>Valor</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            require_once 'conexao.php';
                            $stmt = $pdo->prepare("SELECT * FROM transacoes WHERE usuario_id = ? ORDER BY data_hora DESC");
                            $stmt->execute([$_SESSION['usuario_id']]);
                            $transacoes = $stmt->fetchAll();

                            foreach ($transacoes as $t) {
                                $classe = ($t['tipo'] == 'Deposito') ? 'text-success' : 'text-danger';
                                echo "<tr>";
                                echo "<td>" . date('d/m/Y H:i', strtotime($t['data_hora'])) . "</td>";
                                echo "<td class='$classe'>" . $t['tipo'] . "</td>";
                                echo "<td>R$ " . number_format($t['valor'], 2, ',', '.') . "</td>";
                                echo "</tr>";
                            }
                            ?>
                        </tbody>
                    </table>

                    <a href="sair.php" class="btn btn-danger">Sair</a>   

                    <?php

                    ?>
                </div>
            </div>
        </div>
    </main>
</body>
</html>