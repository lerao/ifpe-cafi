<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php
        if (isset($_GET['msg'])) {
            echo '<font color=red>'. 
                $_GET['msg']
                . "</font>";
        };
    ?>
    
    <form action="validar_garcom.php" 
            method="POST">

            <input type="text" name="usuario"
                placeholder="Login">
            <br>
            <input type="password" name="senha"
                placeholder="Senha">
            <br>
            <input type="submit" value="Entrar no PDV">

    </form>
</body>
</html>















<?php






/*
$nascimento = 1990;
$ano = 2020; 

function calcularIdade() {
    $GLOBALS['idade'] = $GLOBALS['ano'] - $GLOBALS['nascimento'];
}

function calcularIdadeSemGlobal($ano, $nasc) {
    $idade = $ano - $nasc;
}

calcularIdade();
echo $idade;
*/





/*
#Descrevendo uma pessoa
$dados = array("Fulano", 36, "Afogados");
$dados_com_chave = array("nome" => "Fulano", 
                        "idade" => 36, 
                        "cidade" => "Afogados");

print_r($dados);
echo "<hr />";
print_r($dados_com_chave);

 */
























//$new = htmlspecialchars("<a href='test'>Test</a>", ENT_QUOTES);
//echo $new; // &lt;a href=&#039;test&#039;&gt;Test&lt;/a&gt;

//var_dump($_SERVER);
?>