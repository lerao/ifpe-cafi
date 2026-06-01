<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

class Auth
{
    private string $username = 'admin';
    private string $password = '123';

    public function login(string $username, string $password): bool
    {
        if ($username === $this->username && $password === $this->password) {
            $_SESSION['user'] = $username;
            return true;
        }

        return false;
    }

    public function logout(): void
    {
        $_SESSION = [];
        if (session_status() === PHP_SESSION_ACTIVE) {
            session_destroy();
        }
    }

    public function check(): bool
    {
        return !empty($_SESSION['user']);
    }

    public function requireLogin(): void
    {
        if (!$this->check()) {
            header('Location: index.php');
            exit;
        }
    }

    public function currentUser(): ?string
    {
        return $this->check() ? (string) $_SESSION['user'] : null;
    }
}

class Conta {
    protected float $saldo = 0.0;
    protected array $operacoes = [];

    public function __construct(float $saldo = 0.0, array $operacoes = [])
    {
        $this->saldo = $saldo;
        $this->operacoes = $operacoes;
    }

    public function getSaldo(): float
    {
        return $this->saldo;
    }

    public function toArray(): array
    {
        return [
            'saldo' => $this->saldo,
            'operacoes' => $this->operacoes,
        ];
    }

    public static function fromArray(array $data): static
    {
        return new static(
            $data['saldo'] ?? 0.0,
            $data['operacoes'] ?? []
        );
    }
}

trait Acoes {
    public function depositar($valor){
        $this->saldo += $valor;
        $this->adicionarOperacao('Depósito', $valor);
    }

    public function sacar($valor){
        if($this->saldo >= $valor){
            $this->saldo -= $valor;
            $this->adicionarOperacao('Saque', $valor);
        }
    }
}

trait consultaExtrato{

    public function adicionarOperacao(string $tipo, float $valor): void
    {
        $this->operacoes[] = [
            'tipo' => $tipo,
            'valor' => $valor,
            'data' => (new DateTime('now', new DateTimeZone('America/Sao_Paulo')))->format('d/m/Y H:i:s'),
        ];
    }

    public function getOperacoes(): array
    {
        return $this->operacoes;
    }

    public function gerarExtrato(): array
    {
        return $this->getOperacoes();
    }
}

class ContaCorrente extends Conta{
    use Acoes, consultaExtrato;
}
