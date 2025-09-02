

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    matricula = len(funcionarios) + 1
    funcionarios[matricula] = {"nome": nome, "cargo": cargo, "salario": salario}
    print("matricula Nº:  ", matricula)
    print("Funcionário ",  nome, "matricula Nº ", matricula, "cadastrado com sucesso!")


def consultar_funcionario():
    matricula = int(input("Digite a matrícula do funcionário: "))
    if matricula in funcionarios:
        print(f"Nome: {funcionarios[matricula]['nome']}")
        print(f"Cargo: {funcionarios[matricula]['cargo']}")
        print(f"Salário: R${funcionarios[matricula]['salario']:.2f}")
    else:
        print("Funcionário não encontrado!")

def excluir_funcionario():
    matricula = int(input("Digite a matrícula do funcionário: "))
    if matricula in funcionarios:
        del funcionarios[matricula]
        print("Funcionário excluído com sucesso!")
    else:
        print("Funcionário não encontrado!")

def listar_funcionarios():
    if funcionarios:
        print("Lista de Funcionários:")
        for matricula, funcionario in funcionarios.items():
            print(f"Matrícula: {matricula}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: R${funcionario['salario']:.2f}")
            print("-" * 30)
    else:
        print("Nenhum funcionário cadastrado!")

def main():
    while True:
        print("Menu:")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Excluir Funcionário")
        print("4. Listar Funcionários")
        print("5. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            consultar_funcionario()
        elif opcao == "3":
            excluir_funcionario()
        elif opcao == "4":
            listar_funcionarios()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()