import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
from class_Autentica import *
from class_sistema import *

#######



# Dados a serem armazenados no JSON
contactsList = {
    "cliente": {
        "cliente1": "senha1",
        "cliente2": "senha2"
    },
    "funcionario": {
        "funcionario1": "senha3",
        "funcionario2": "senha4"
    }
}

# Nome do arquivo JSON
nome_arquivo = "dados_usuarios.json"

# Escrever os dados no arquivo JSON
with open(nome_arquivo, 'w') as arquivo:
    json.dump(contactsList, arquivo, indent=4)

print(f"Arquivo JSON '{nome_arquivo}' gerado com sucesso.")


contatos = {}
contatos['ANA'] = '1010-11111'
contatos['BIA'] = 'agora'
f = open('./lista.json','w')
json.dump(contatos, f)
f.close()

f = open('./lista.json', 'r')
contatos = json.load(f)
f.close
for nome, telefone in contatos.items():
    print('Nome: {} \nTelefone: {}'.format(nome,telefone))
