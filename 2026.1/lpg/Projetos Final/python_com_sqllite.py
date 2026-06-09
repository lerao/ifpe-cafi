import sqlite3

# 1. Conectar ao banco de dados (cria o arquivo 'empresa.db' se não existir)
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# 2. Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL
    )
''')

# 3. Inserir dados
# Sempre use '? ' para evitar ataques de SQL Injection
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", 
               ('Ana Silva', 'Desenvolvedora', 8500.00))

# Salvar as alterações (commit)
conexao.commit()

# 4. Consultar dados
cursor.execute("SELECT * FROM funcionarios Where sabor = ?", ('Mussarela',))
resultados = cursor.fetchall()

for linha in resultados:
    print(f"ID: {linha[0]} | Nome: {linha[1]} | Cargo: {linha[2]} | Salário: R$ {linha[3]:.2f}")

# 5. Fechar conexão
conexao.close()