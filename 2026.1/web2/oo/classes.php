<?php
  class Conta {
    public $saldo = 0;
    public function getSaldo(){
      echo "Saldo Atual: {$this->saldo}";
    }
  }
  
  trait Acoes {
    public function depositar($valor){
      $this->saldo += $valor;
    }
    public function sacar($valor){
      if($this->saldo >= $valor){
        $this->saldo -= $valor;
      }
    }
  }

  trait consultaExtrato{
    public function getSaldo(){
      echo "Saldo Disponivel para saque:{$this->saldo}<br>";
    }
    public function gerarExtrato($periodo){
      echo "Gerando extrato período $periodo aguarde...";
    }
  }

  class ContaCorrente extends Conta{
    use Acoes, consultaExtrato;
  }

  $valor = $_POST['valor'];
  $acao = $_POST['acao'];   
  
  $o = new ContaCorrente();
  $o->getSaldo();
  if ($acao == 'depositar') {
    $o->depositar($valor);
    $o->getSaldo();
  } else if ($acao == 'sacar') {
    $o->sacar($valor);
    $o->getSaldo();
  }
  date_default_timezone_set('America/Sao_Paulo');
  $data = new DateTime();
  $periodo = $data->format('d/m/Y H:i:s');
  $o->gerarExtrato($periodo);
?>

  ?>