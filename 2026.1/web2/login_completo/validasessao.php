<?php
session_start();

if (!isset($_SESSION['logado'])) {
    header('Location: index.php?msg=Faça login para acessar a página principal.');
    die();
}

?>