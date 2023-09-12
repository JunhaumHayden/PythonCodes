from random import randint, shuffle

# Defina os naipes e valores das cartas
naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']




#suits = 'shcd'          # naipes das cartas
#ranks = 'AKQJT98765432' # cartas
deck = []               # deck de cartas
player_hand = []        # guarda as cartas dos players
nop = 9                 # numero de players

while True:
    # Gerando o deck de cartas com estrutura de repetição
    #for suit in suits:               # para cada naipe...
    #    for rank in ranks:           # sera adiconada uma carta...
    #        deck.append(rank + suit) # via funcao 'append()'
    
    # Gerando o deck de cartas com List Comprehension
    deck = [(valor, naipe) for valor in valores for naipe in naipes]
    
    shuffle(deck)                    # reembaralhar
    player_hand = []
    out_cards = []

    #print(deck)
    #print(player_hand)
    #print(out_cards)

 # def_hands, definir maos dos players

    for def_hands in range(0, nop):  
        player_hand.append(deck.pop(0)), player_hand.append(deck.pop(0))
    
    #print('deck')
    #print(deck)
    #print('\n')
    #print(player_hand)
    #print(out_cards)
    

 # mostrar as maos dos players
    x = 0
    for show in range(0, nop):       
        print(f'Player{show+1}: {player_hand[x]} {player_hand[x+1]}')
        x += 2

    board = []
    board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)) # definindo board
    print(f'{" " * 7}Board: {board[0]} {board[1]} {board[2]} {board[3]} {board[4]}')

    entrada = input("Zero para Encerrar: ") # apenas para nao entrar em loop infinito
    if entrada == '0':
        break