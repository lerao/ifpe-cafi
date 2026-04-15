<?php
//Faça uma tabela com 100 linhas e o conteudo de cada 
// linha é o número de linha.
?>
<table>
    <thead>
        <tr>
            <th>Número da Linha</th>
        </tr>
    </thead>
    <tbody>
        <?php
        // O laço inicia em 1 e vai até 100
        for ($i = 1; $i <= 100; $i++) {
            echo "<tr>";
            echo "<td>$i</td>";
            echo "</tr>";
        }
        ?>
    </tbody>
</table>