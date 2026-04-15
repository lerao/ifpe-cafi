<?php
//Faça o estilo zebrado (tom claro, tom escuro, tom claro,
//  tom escuro...) a cada duas linhas da tabela
?>

<style>
    table {
        border-collapse: collapse;
        width: 250px;
        font-family: Arial, sans-serif;
    }
    td {
        border: 1px solid #ccc;
        padding: 8px;
        text-align: center;
    }
    /* Classe para o tom escuro */
    .tom-escuro {
        background-color: #d1d1d1; /* Cinza mais forte */
    }
    /* Classe para o tom claro */
    .tom-claro {
        background-color: #f9f9f9; /* Cinza bem clarinho */
    }
</style>

<table>
    <thead>
        <tr>
            <th>Contador</th>
        </tr>
    </thead>
    <tbody>
        <?php
        for ($i = 1; $i <= 100; $i++) {
            // Lógica: Se o resto da divisão por 4 for 1 ou 2 -> Tom Claro
            // Se for 3 ou 0 -> Tom Escuro
            if ($i % 4 == 1 || $i % 4 == 2) {
                $classe = "tom-claro";
            } else {
                $classe = "tom-escuro";
            }

            echo "<tr class='$classe'>";
            echo "<td>Linha $i</td>";
            echo "</tr>";
        }
        ?>
    </tbody>
</table>