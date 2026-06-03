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
                    <h1><mark>Principal</mark></h1>
                    <h1>Bem Vindo <?php echo $_SESSION['usuario']; ?></h1>
                    
                    <p>Você está logado com sucesso!</p>

                    <hr>
                    <h3>Realizar Transação</h3>
                    <form action="processa_transacao.php" method="post">
                        <div class="mb-3">
                            <label for="tipo" class="form-label">Tipo</label>
                            <select name="tipo" id="tipo" class="form-select">
                                <option value="Deposito">Depósito</option>
                                <option value="Saque">Saque</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="valor" class="form-label">Valor</label>
                            <input type="number" step="0.01" class="form-control" id="valor" name="valor" required>
                        </div>
                        <button type="submit" class="btn btn-success">Confirmar</button>
                    </form>
                    <hr>

                    <a href="sair.php" class="btn btn-danger">Sair</a>   

                    <?php

                    ?>
                </div>
            </div>
        </div>
    </main>
</body>
</html>