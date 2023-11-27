import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import requests
from GoogleNews import GoogleNews
import pandas as pd
#######
news = GoogleNews()
news.setlang('pt')

contatos = {}
contatos["user1"] = "senha"
contatos["user2"] = "senha"
contatos["admin"] = "senha"
f = open('usuarios.json','w')
json.dump(contatos, f)
f.close()

class Noticia:
    def __init__(self, data, assunto, categoria, texto):
        self.data = data
        self.assunto = assunto
        self.categoria = categoria
        self.texto = texto

class AppNoticias:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Notícias")
        self.texto_noticias = None  # Adiciona uma variável de instância para armazenar o widget de texto
        self.df = pd.DataFrame()  # Variável para armazenar as notícias
        self.login()

    def login(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        tk.Label(self.login_frame, text="Login").grid(row=0, column=0)
        tk.Label(self.login_frame, text="Usuário:").grid(row=1, column=0)
        tk.Label(self.login_frame, text="Senha:").grid(row=2, column=0)

        self.usuario_entry = tk.Entry(self.login_frame)
        self.senha_entry = tk.Entry(self.login_frame, show="*")

        self.usuario_entry.grid(row=1, column=1)
        self.senha_entry.grid(row=2, column=1)

        tk.Button(self.login_frame, text="Entrar", command=self.verificar_login).grid(row=3, column=1, pady=10)

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if self.autenticar(usuario, senha):
            self.login_frame.destroy()  # Destruir o frame de login
            self.exibir_interface()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos. Tente novamente.")

    def autenticar(self, usuario, senha):
        try:
            with open("usuarios.json", "r") as file:
                usuarios = json.load(file)

            # Verifica se o usuário e senha correspondem
            return usuario in usuarios and usuarios[usuario] == senha
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de usuários não encontrado.")
            return False
        except json.JSONDecodeError:
            messagebox.showerror("Erro", "Erro ao decodificar o arquivo JSON.")
            return False

    def exibir_interface(self):

        
        self.interface_frame = tk.Frame(self.root)
        self.interface_frame.pack(padx=20, pady=20)

        # Elementos da interface (labels, entry, botões)
        tk.Label(self.interface_frame, text="Filtro de Notícias").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.interface_frame, text="Data Início:").grid(row=1, column=0)
        self.data_inicio_entry = tk.Entry(self.interface_frame)
        self.data_inicio_entry.grid(row=1, column=1)

        tk.Label(self.interface_frame, text="Data Fim:").grid(row=2, column=0)
        self.data_fim_entry = tk.Entry(self.interface_frame)
        self.data_fim_entry.grid(row=2, column=1)

        tk.Label(self.interface_frame, text="Assunto:").grid(row=3, column=0)
        self.assunto_entry = tk.Entry(self.interface_frame)
        self.assunto_entry.grid(row=3, column=1)

        # tk.Label(self.interface_frame, text="Categoria:").grid(row=4, column=0)
        # # Lista flutuante (dropdown) para o campo 'categoria'
        # categorias = ["Esporte", "Política", "Bolsa de Valores", "Entretenimento", "Diversão"]
        # self.categoria_combobox = ttk.Combobox(self.interface_frame, values=categorias)
        # self.categoria_combobox.grid(row=4, column=1)

        tk.Label(self.interface_frame, text="Categoria:").grid(row=4, column=0)
        self.categoria_entry = tk.Entry(self.interface_frame)
        self.categoria_entry.grid(row=4, column=1)

        tk.Label(self.interface_frame, text="Notícia:").grid(row=5, column=0)
        self.texto_entry = tk.Entry(self.interface_frame, width=50)
        self.texto_entry.grid(row=5, column=1, columnspan=2)

        tk.Button(self.interface_frame, text="Adicionar Notícia", command=self.adicionar_noticia).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.interface_frame, text="Buscar Notícias", command=self.buscar_noticias).grid(row=7, column=0, columnspan=2, pady=10)


        # Adiciona um widget de texto à interface
        self.texto_noticias = tk.Text(self.interface_frame, height=110, width=60, wrap=tk.WORD)
        self.texto_noticias.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")


        # Configuração para que a coluna e a linha se expandam conforme o tamanho da janela
        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.rowconfigure(8, weight=1)

         # Adiciona um botão "Sair"
        tk.Button(self.interface_frame, text="Sair", command=self.encerrar_aplicativo).grid(row=9, column=0, columnspan=2, pady=10)


    def encerrar_aplicativo(self):
        self.root.destroy()  # Destroi a janela principal, encerrando o aplicativo

    def adicionar_noticia(self):
        # Lógica para adicionar notícia à lista ou dicionário
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        assunto = self.assunto_entry.get()
        categoria = self.categoria_entry.get()
        texto = self.texto_entry.get()

        noticia = Noticia(data, assunto, categoria, texto)

        f = open('post_news.json','w')
        json.dump(noticia, f)
        f.close()

        messagebox.showinfo("Sucesso", "Notícia adicionada com sucesso.")

    def buscar_noticias(self):
        
        data_inicio = self.data_inicio_entry.get()
        data_fim = self.data_fim_entry.get()
        assunto = self.assunto_entry.get()
        categoria = self.categoria_entry.get()

        print(data_inicio)
        print(data_fim)
        print(assunto)
        #print(categoria)
        print('printando com Pandas')

        # Limpar o conteúdo anterior no widget de texto
        self.texto_noticias.delete("1.0", tk.END)

        news.search(assunto+' '+categoria)
        news.set_time_range(data_inicio,data_fim)
        # Iterar sobre as notícias e adicionar ao widget de texto
        for i in range(1, 2):
            news.getpage(i)
            result = news.result(assunto+' '+categoria)
            links = news.get_links()
            df = pd.DataFrame(result)
            # Adicionar notícias ao widget de texto
            text_news = df.to_string(index=False, header=False)
            self.texto_noticias.insert(tk.END, f"---------PAGE {i}-----------\n{text_news}\n\n*******************************************\n\n")
            print(df)
            df = pd.DataFrame()  # Isso cria um DataFrame vazio
            print('dataframe apagado')
            print(df)


       


if __name__ == "__main__":
    root = tk.Tk()
    app = AppNoticias(root)
    root.mainloop()
