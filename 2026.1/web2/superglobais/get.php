<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    //Testando o GET
    print_r($_GET);
    echo "<hr>";
    echo ($_GET['msg']);
    echo "<hr>";
    echo (isset($_GET['msg']) === '');
    ?>
    <form method="GET">
        <input type="text" name="msg">
        <input type="submit" >
</form>
</body>
</html>