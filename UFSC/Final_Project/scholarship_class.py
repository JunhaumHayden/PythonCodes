from student_class import Students


class Scholarship(Students):
    """Classe de estudantes Bolsistas"""
    def __init__(self, tipo, nome, idade, cpf, fone, nome_resp, curso, mensalidade, desconto):
        super().__init__(tipo, nome, idade, cpf, fone, nome_resp, curso, mensalidade)
        self.desconto = desconto
        

    def get_desconto(self):
        return self.desconto
    def set_desconto(self, desconto):
        self.desconto = desconto


    def get_mensalidade(self):
        return (self.mensalidade - ((self.mensalidade * self.desconto) / 100))
    def set_mensalidade(self,mensalidade):
        self.mensalidade = mensalidade

    def __str__(self):
        super().__str__()
        print(f"desconto: {self.desconto}")

    def get_informacoes(self):
        print('-' * 30)
        print("desconto:", self.desconto)
        print( )
        print( )
    

        