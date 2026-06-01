<?php
require_once 'classes.php';
$auth = new Auth();
$auth->logout();
header('Location: index.php');
exit;
