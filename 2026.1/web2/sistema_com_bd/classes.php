<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

class Auth
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function login(string $username, string $password): bool
    {
        $stmt = $this->pdo->prepare("SELECT * FROM usuarios WHERE usuario = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch();

        if ($user && $password == $user['senha']) {
            $_SESSION['usuario_id'] = $user['id'];
            $_SESSION['usuario'] = $user['nome'];
            $_SESSION['logado'] = true;
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
        return !empty($_SESSION['logado']);
    }

    public function requireLogin(): void
    {
        if (!$this->check()) {
            header('Location: index.php?msg=Faça login para acessar o sistema.');
            exit;
        }
    }

    public function currentUser(): ?string
    {
        return $this->check() ? (string) $_SESSION['usuario'] : null;
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
}

trait Acoes {
    public function depositar(PDO $pdo, int $usuario_id, float $valor): bool
    {
        $stmt = $pdo->prepare("INSERT INTO transacoes (usuario_id, tipo, valor) VALUES (?, 'Deposito', ?)");
        return $stmt->execute([$usuario_id, $valor]);
    }

    public function sacar(PDO $pdo, int $usuario_id, float $valor): bool
    {
        $stmt = $pdo->prepare("INSERT INTO transacoes (usuario_id, tipo, valor) VALUES (?, 'Saque', ?)");
        return $stmt->execute([$usuario_id, $valor]);
    }
}

trait consultaExtrato {
    public function getOperacoes(PDO $pdo, int $usuario_id): array
    {
        $stmt = $pdo->prepare("SELECT * FROM transacoes WHERE usuario_id = ? ORDER BY data_hora DESC");
        $stmt->execute([$usuario_id]);
        return $stmt->fetchAll();
    }
}

class ContaCorrente extends Conta {
    use Acoes, consultaExtrato;

    public static function getSaldoAtual(PDO $pdo, int $usuario_id): float
    {
        $stmt = $pdo->prepare("SELECT 
            SUM(CASE WHEN tipo = 'Deposito' THEN valor ELSE -valor END) as saldo 
            FROM transacoes WHERE usuario_id = ?");
        $stmt->execute([$usuario_id]);
        $res = $stmt->fetch();
        return (float) ($res['saldo'] ?? 0.0);
    }
}
