<?php
require_once 'classes.php';
$auth = new Auth();
if ($auth->check()) {
    header('Location: principal.php');
    exit;
}
$error = isset($_GET['error']);
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body class="bg-body-secondary">
<main class="container py-5">
    <div class="row justify-content-center">
        <div class="col-12 col-sm-10 col-md-8 col-lg-6">
            <div class="card shadow-sm border-0">
                <div class="card-body p-4">
                    <h1 class="h3 mb-3 text-center">Entrar no sistema</h1>
                    <p class="text-center text-muted mb-4">Usuário <strong>admin</strong> e senha <strong>123</strong>.</p>
                    <?php if ($error): ?>
                        <div class="alert alert-danger" role="alert">
                            Usuário ou senha incorretos. Tente novamente.
                        </div>
                    <?php endif; ?>
                    <form action="validalogin.php" method="post" class="row g-3">
                        <div class="col-12">
                            <label for="username" class="form-label">Usuário</label>
                            <input type="text" id="username" name="username" class="form-control" placeholder="admin" required autofocus>
                        </div>
                        <div class="col-12">
                            <label for="password" class="form-label">Senha</label>
                            <input type="password" id="password" name="password" class="form-control" placeholder="123" required>
                        </div>
                        <div class="col-12 d-grid">
                            <button type="submit" class="btn btn-primary btn-lg">Entrar</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</main>
</body>
</html>
