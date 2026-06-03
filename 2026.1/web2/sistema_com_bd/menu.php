<?php
include_once 'validasessao.php';
$current_page = basename($_SERVER['PHP_SELF']);
?>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
    <div class="container">
        <a class="navbar-brand" href="principal.php">Sistema Bancário</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link <?= $current_page == 'principal.php' ? 'active' : '' ?>" href="principal.php">Principal</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link <?= $current_page == 'historico.php' ? 'active' : '' ?>" href="historico.php">Histórico</a>
                </li>
            </ul>
            <div class="d-flex align-items-center">
                <span class="navbar-text text-white me-3">Olá, <?= htmlspecialchars($_SESSION['usuario'] ?? 'Usuário') ?></span>
                <a class="btn btn-outline-light btn-sm" href="sair.php">Sair</a>
            </div>
        </div>
    </div>
</nav>
