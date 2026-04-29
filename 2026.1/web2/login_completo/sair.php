<?php
session_start();
session_unset();
session_destroy();

header('Location: index.php?msg=Você saiu com sucesso.');
die();

?>