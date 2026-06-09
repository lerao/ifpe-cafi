CREATE DATABASE IF NOT EXISTS sistema_bancario;
USE sistema_bancario;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    tipo ENUM('Deposito', 'Saque') NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Usuário inicial (senha: admin123)
-- Em uma aplicação real, usaríamos password_hash. Para esta aula inicial, manteremos simples.
INSERT INTO usuarios (nome, usuario, senha) VALUES ('Administrador', 'admin', 'admin123');
