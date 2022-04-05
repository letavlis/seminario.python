from Pessoa import Pessoa
import db


def adicionar_pessoa(nome, email, telefone, endereco, cpf):
    p = Pessoa(nome, email, telefone, endereco, cpf)
    db.adicionar(p)


def mostrar_pessoa():
    for pessoa in db.get_pessoa():
        p = pessoa
        print(p)


def atualizar_pessoa(idPessoa, email, telefone, endereco):
    db.atualizar(idPessoa, email, telefone, endereco)


def remover_pessoa(idPessoa):
    db.remover(idPessoa)
