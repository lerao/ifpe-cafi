<?php
require_once 'classes.php';
$auth = new Auth();

$username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_SPECIAL_CHARS) ?? '';
$password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_SPECIAL_CHARS) ?? '';

if ($auth->login($username, $password)) {
    header('Location: principal.php');
    exit;
}

header('Location: index.php?error=1');
exit;
