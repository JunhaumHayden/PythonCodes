class School:
    """Classe principal"""
    def __init__(self, tipo, nome, idade, cpf, fone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.fone = fone
        self.tipo = tipo

    def get_nome(self):
        return self.nome    
    def set_nome(self,nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf    
    def set_cpf(self,cpf):
        self.cpf = cpf

    def get_idade(self):
        return self.idade    
    def set_idade(self,idade):
        self.idade = idade

    def get_fone(self):
        return self.fone    
    def set_fone(self,fone):
        self.fone = fone
    
    def get_tipo(self):
        return self.tipo    
    def set_tipo(self,tipo):
        self.tipo = tipo 


    def get_desconto(self):
        return 0
    def set_desconto(self,desconto):
        print(f' Aluno não elegível ao desconto')

    def get_mensalidade(self):
        return 0    
    def set_mensalidade(self,mensalidade):
        print(f' Pessoa não elegível ao desconto')

    def get_curso(self):
        return 0
    def set_curso(self,curso):
        print(f' Aluno não elegível ao curso')

    def __str__(self):
        print(f" \nTipo: {self.tipo} \nNome: {self.nome} \nIdade: {self.idade} \ncpf: {self.cpf} \nfone: {self.fone} ")
    
