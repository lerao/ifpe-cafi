<?php
//Adicione uma coluna na tabela anterior e mostre o mês e o
//  ano (Por extenso) sendo que a primeira linha inicia com 
// janeiro de 2000 e vai aumentando um mês por linha. 
// (depois de dez/2000 vem jan/2001).
?>



<?php
$meses = [
    1 => "Janeiro", 2 => "Fevereiro", 3 => "Março", 4 => "Abril",
    5 => "Maio", 6 => "Junho", 7 => "Julho", 8 => "Agosto",
    9 => "Setembro", 10 => "Outubro", 11 => "Novembro", 12 => "Dezembro"
];

// Valores iniciais
$mesAtual = 1;
$anoAtual = 2000;
?>

<style>
    table {
        border-collapse: collapse;
        width: 400px;
        font-family: Arial, sans-serif;
    }
    td, th {
        border: 1px solid #ccc;
        padding: 8px;
        text-align: left;
    }
    .tom-claro { background-color: #ffffff; }
    .tom-escuro { background-color: #f2f2f2; }
</style>

<table>
    <thead>
        <tr>
            <th>Linha</th>
            <th>Mês e Ano</th>
        </tr>
    </thead>
    <tbody>
        <?php
        for ($i = 1; $i <= 100; $i++) {
            // Lógica do zebrado a cada duas linhas
            if ($i % 4 == 1 || $i % 4 == 2) {
                $classe = "tom-claro";
            } else {
                $classe = "tom-escuro";
            }

            echo "<tr class='$classe'>";
            echo "<td>$i</td>";
            echo "<td>" . $meses[$mesAtual] . " de " . $anoAtual . "</td>";
            echo "</tr>";

            // Lógica manual para aumentar o mês
            $mesAtual++;

            // Se o mês passar de 12, volta para 1 e aumenta o ano
            if ($mesAtual > 12) {
                $mesAtual = 1;
                $anoAtual++;
            }
        }
        ?>
    </tbody>
</table>
?>