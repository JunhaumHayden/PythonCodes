import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url)
data = resposta.json()
#print(data)

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']
flag = True
while flag:
        valor_secreto = random.choice(data)
        print('='*30)
        print('\nAdivinhe a palavra secreta ou digite 0 (zero) para sair\n')
        print('-'*30)
        print(f'A palavra secreta tem {len(palavra_secreta)} letras')
        chute = input(f'Dica da palavra secreta -> {dica}: ')
        if chute == '0':
             print('Encerrando o jogo...')
             flag = False
        elif chute == palavra_secreta:
            print('='*30)
            print('Acertou!')
        else:
            print('*'*30)
            print(f'Errou!!!/n a palavra secreta é: {palavra_secreta}')