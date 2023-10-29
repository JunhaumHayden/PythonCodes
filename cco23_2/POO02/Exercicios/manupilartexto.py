import json

def writing():
    arq = open('./textes02.txt', 'w')
    texto= """ 
    Lista de Alunos
    ---
    Joao Silva
    Jose Lima
    Maria das Dores
    """
    arq.write(texto)
    arq.close

def add_file_through_list():
    arq = open("./textes002.txt", 'w')
    texto = []
    texto.append('Lista de Alunos\n')
    texto.append('---\n')
    texto.append('Ana\n')
    texto.append('Bia\n')
    texto.append('Clara\n')
    arq.writelines(texto)
    arq.close()

def read_file():
    arq = open("./textes.txt", 'r')
    text = arq.read()
    print(text)
    arq.close()

#with JSON files

def add_file_json():
    contatos = {}
    contatos['ANA'] = '1010-11111'
    contatos['BIA'] = '2020-2222'
    f = open('listaTelefonica.txt','w')
    json.dump(contatos, f)
    f.close()

def read_file_json():
    f = open('listaTelefonica.txt', 'r')
    contatos = json.load(f)
    f.close
    for nome, telefone in contatos.items():
            print('Nome: {} \nTelefone: {}'.format(nome,telefone))

read_file_json()
