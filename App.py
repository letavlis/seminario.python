import db
import Repositorio as repoP
import os


def main():
    print("1. adicionar pessoa")
    print("2. ver pessoas adicionadas")
    print("3. atualizar pessoa")
    print("4. remover pessoa")
    print("5. sair")
    opcao = int(input("escolha uma opçao: "))

    if opcao == 1:
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        cpf = input("Cpf: ")

        repoP.adicionar_pessoa(nome, email, telefone, endereco, cpf)
    elif opcao == 2:
        repoP.mostrar_pessoa()
    elif opcao == 3:
        repoP.mostrar_pessoa()
        id_pessoa = int(input("Digite o id da pessoa que deseja atualizar: "))
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereco: ")
        repoP.atualizar_pessoa(id_pessoa, email, telefone, endereco)
    elif opcao == 4:
        repoP.mostrar_pessoa()
        id_pessoa = int(input("Digite o id da pessoa que deseja remover: "))
        repoP.remover_pessoa(id_pessoa)
    elif opcao == 5:
        exit(0)


if __name__ == "__main__":
    db.cria_tabela()

    main()
