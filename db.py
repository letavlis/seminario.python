import sqlite3

# conexão com banco de dados
conn = sqlite3.connect("Pessoa.db")

cursor = conn.cursor()


# cria tabela pessoa se não existir
def cria_tabela():
    conn.execute(
        """create table if not exists pessoa(
        id integer primary key autoincrement,
        nome varchar(45) not null,
        email varchar(45) not null,
        telefone varchar(11) not null,
        endereco varchar(45) not null,
        cpf varchar(11) not null)
    """)


# adiciona pessoa
def adicionar(pessoa):
    conn.execute("insert into pessoa (nome, email, telefone, endereco, cpf) values(?,?,?,?,?)",
                 (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.endereco, pessoa.cpf))
    conn.commit()


def atualizar(id_pessoa, email, telefone, endereco):
    conn.execute("update pessoa set email=?, telefone=?, endereco=? where id=?",
                 (email, telefone, endereco, id_pessoa))
    conn.commit()


def remover(id_pessoa):
    conn.execute("delete from pessoa where id = ?", (id_pessoa,))
    conn.commit()


def get_pessoa():
    cursor.execute("select * from pessoa")
    return cursor.fetchall()
