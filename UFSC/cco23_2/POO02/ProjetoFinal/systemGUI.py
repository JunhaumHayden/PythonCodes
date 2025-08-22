#operacional: validando login e senha e retornando o ID 30/11/2023. .
import tkinter as tk
from tkinter import messagebox
import json

class SistemaLavagemCarros:
    """Classe para instanciar as janelas do sistema"""
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Lavagem de Carros")

        # Variáveis para armazenar login e senha
        self.login_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        # Carregar informações de login e senha do arquivo JSON
        self.usuarios = self.carregar_usuarios()

        # Tela de Boas-vindas
        self.label_welcome = tk.Label(root, text="Bem-vindo ao Sistema de Lavagem de Carros!", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        # Entradas para login e senha
        self.label_login = tk.Label(root, text="Login:")
        self.entry_login = tk.Entry(root, textvariable=self.login_var)

        self.label_senha = tk.Label(root, text="Senha:")
        self.entry_senha = tk.Entry(root, textvariable=self.senha_var, show="*")

        self.label_login.pack(pady=5)
        self.entry_login.pack(pady=5)
        self.label_senha.pack(pady=5)
        self.entry_senha.pack(pady=5)

        # Botões de Login e Cadastro
        self.button_login = tk.Button(root, text="Login", command=self.autenticar_usuario)
        self.button_login.pack(pady=10)

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.pack(pady=10)

    def carregar_usuarios(self):
        try:
            with open("./pythonCode/cco23_2/POO02/ProjetoFinal/usuarios.json", "r") as file:
                listUsers = json.load(file)
                return listUsers
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'usuarios.json' não encontrado.")
            self.root.destroy()

    def salvar_usuarios(self):
        with open("./pythonCode/cco23_2/POO02/ProjetoFinal/usuarios.json", "w") as file:
            json.dump(self.usuarios, file, indent=2)

    def autenticar_usuario(self):
         # Verificar o tipo de usuário (cliente ou funcionário)
        tipo_usuario = self.verificar_tipo_usuario()

        # Simular autenticação
        login_digitado = self.login_var.get()
        senha_digitada = self.senha_var.get()

         # Verifique se o tipo de usuário está presente nos dados
        if tipo_usuario in self.usuarios and login_digitado in self.usuarios[tipo_usuario]:
            if self.usuarios[tipo_usuario][login_digitado]["senha"] == senha_digitada:
                messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {tipo_usuario.capitalize()}!")
                id_usuario = self.usuarios[tipo_usuario][login_digitado]["id"]
                if tipo_usuario == "cliente":
                    self.login_frame.destroy()  # Destruir o frame de login
                    self.abrir_interface_cliente(id_usuario)
                elif tipo_usuario == "funcionario":
                    self.abrir_interface_funcionario(id_usuario)
            else:
                messagebox.showerror("Erro de login", "Credenciais inválidas. Tente novamente.")
        else:
            messagebox.showerror("Erro de login", f"Usuário {tipo_usuario} não encontrado.")


    def abrir_interface_cliente(self, id_cliente):
        # Lógica para abrir a interface do cliente com base no ID
        print(f"Abrindo interface do cliente ID {id_cliente}")



    def verificar_tipo_usuario(self):
        # Lógica simples para verificar o tipo de usuário com base no login
        login_digitado = self.login_var.get().lower()

        if "cliente" in login_digitado:
            return "cliente"
        elif "funcionario" in login_digitado:
            return "funcionario"
        else:
            return "desconhecido"

    def cadastrar_usuario(self):
        novo_login = self.login_var.get()
        novo_senha = self.senha_var.get()

        tipo_usuario = self.verificar_tipo_usuario()

        if novo_login not in self.usuarios[tipo_usuario]:
            self.usuarios[tipo_usuario][novo_login] = novo_senha

            # Gere um novo ID para o usuário
            novo_id = len(self.usuarios[tipo_usuario]) + 1

            # Adiciona o novo usuário ao dicionário
            self.usuarios[tipo_usuario][novo_login] = {"id": novo_id, "senha": novo_senha}

            # Salva os usuários atualizados no arquivo JSON
            self.salvar_usuarios()
            messagebox.showinfo("Cadastro bem-sucedido", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro de cadastro", "Este login já está em uso. Escolha outro.")

    def abrir_interface_cliente(self, id_client):
        # Lógica para abrir a interface do cliente
        # Implemente conforme necessário
        print(f"Abrir interface do cliente ID: {id_client}")

    def abrir_interface_funcionario(self, id_employer):
        # Lógica para abrir a interface do funcionário
        # Implemente conforme necessário
        print(f"Abrir interface do funcionário: ID: {id_employer}")


if __name__ == "__main__":
    import json

# Dados a serem armazenados no JSON
    dados = {
                "cliente": 
                {
                    "cliente1": 
                        {
                            "senha": "senha1",
                            "id": 1
                        },
                    "cliente2": 
                        {
                            "senha": "senha2",
                            "id": 2
                        }
                },
                "funcionario": 
                {
                    "funcionario1": 
                    {
                        "senha": "senha3",
                        "id": 3
                    },
                    "funcionario2": 
                    {
                        "senha": "senha4",
                        "id": 4
                    }
                    }
}

    # Nome do arquivo JSON
    nome_arquivo = "./pythonCode/cco23_2/POO02/ProjetoFinal/usuarios.json"

    # Escrever os dados no arquivo JSON
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"Arquivo JSON '{nome_arquivo}' gerado com sucesso.")

    
    root = tk.Tk()
    sistema = SistemaLavagemCarros(root)
    root.mainloop()
