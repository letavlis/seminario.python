class Pessoa:
    def __init__(self, nome, email, telefone, endereco, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf

    def __repr__(self):
        return "Pessoa({}, {}, {}, {},{}".format(
            self.nome,
            self.email,
            self.telefone,
            self.endereco,
            self.cpf
        )
