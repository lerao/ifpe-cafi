from gerenciador_arquivos import GerenciadorArquivo

def menu():
    print("\n" + "="*30)
    print("      SISTEMA ESCOLAR")
    print("="*30)
    print("1. Cadastrar Aluno e Notas")
    print("2. Listar Alunos e Médias")
    print("3. Verificar Aprovações")
    print("0. Sair")
    print("="*30)

def cadastrar_aluno(db):
    print("\n--- Novo Registro ---")
    nome = input("Nome do Aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    alunos = db.recuperaDados()
    # [Nome, Nota1, Nota2, Nota3]
    alunos.append([nome, n1, n2, n3])
    db.salvarDados(alunos)
    print("Aluno cadastrado!")

def listar_alunos(db):
    print("\n--- Lista de Alunos ---")
    alunos = db.recuperaDados()
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for a in alunos:
        media = (a[1] + a[2] + a[3]) / 3
        print(f"Aluno: {a[0]:15} | Notas: {a[1]}, {a[2]}, {a[3]} | Média: {media:.1f}")

def verificar_aprovacoes(db):
    print("\n--- Status de Aprovação (Média >= 7.0) ---")
    alunos = db.recuperaDados()
    if not alunos: return
    
    for a in alunos:
        media = (a[1] + a[2] + a[3]) / 3
        status = "APROVADO" if media >= 7.0 else "REPROVADO"
        print(f"{a[0]:15} -> Média: {media:4.1f} | Status: {status}")

def principal():
    db_escola = GerenciadorArquivo("alunos.csv")
    
    while True:
        menu()
        opcao = input("Opção: ")
        
        if opcao == "1":
            cadastrar_aluno(db_escola)
        elif opcao == "2":
            listar_alunos(db_escola)
        elif opcao == "3":
            verificar_aprovacoes(db_escola)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    principal()
