import random


#A classe Carta representa uma única carta com um valor e um naipe
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f'{self.valor} de {self.naipe}'

#A classe Deck representa um baralho completo com métodos para embaralhar e distribuir cartas.
class Deck:
    def __init__(self):
        naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartas = [Carta(valor, naipe) for valor in valores for naipe in naipes]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, num_jogadores):
        cartas_por_jogador = len(self.cartas) // num_jogadores
        jogadores = [[] for _ in range(num_jogadores)]
        
        #print(cartas_por_jogador)
        #print('\n')
        #4print(jogadores)

        for i in range(num_jogadores):
            jogadores[i] = self.cartas[i * cartas_por_jogador:(i + 1) * cartas_por_jogador]
            #print('criando jogadores')
            #print(jogadores[i])
        #print(jogadores)
        return jogadores

#main
while True:
# O programa principal (main)d cria um baralho, embaralha as cartas e distribui para nove jogadores.
    #verifica se o script está sendo executado como um programa independente
    # (Quando um script é executado como programa principal, __name__ é definido como "__main__".) 
    # ou se foi importado como um módulo em outro programa
    # (Se for importado como um módulo em outro script, __name__ será o nome do próprio módulo.)
    if __name__ == "__main__": 
        baralho = Deck()
        baralho.embaralhar()

        num_jogadores = 9
        jogadores = baralho.distribuir(num_jogadores)

        for i, mao in enumerate(jogadores, start=1):
            print(f'Jogador {i}: {[str(carta) for carta in mao]}')
        
        entrada = input("Zero para Encerrar: ") # apenas para nao entrar em loop infinito
        if entrada == '0':
            break
