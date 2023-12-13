import tkinter as tk
from tkinter import messagebox
import json
#from datetime import datetime
import datetime
from class_sistema import *




class SistemaLavagemCarros:
    """Classe para instanciar as interface grafica do sistema"""
    def __init__(self, root):
        self.root = root
        self.data_sys = datetime.today()
        self.root.title("Sistema de Lavagem de Carros")
        self.user_type = 'clienteeee'
        self.user_id = 0
        self.cliente = []
        self.login() #main program
        #self.abrir_interface() #just for test

    def program_log(self, message, arquivo_log="./pythonCode/cco23_2/POO02/ProjetoFinal/log.json"):
        # Log para visualizaçao no terminal
        print(message)
    
        # Obtém a data e hora atual
        data_atual = self.data_sys.strftime("%Y%m%d_%H%M")

        # Cria um dicionário com a message e a data
        log_entry = {"data": data_atual, "message": message}
        

        try:
            # Tenta carregar o arquivo existente
            with open(arquivo_log, "r") as file:
                logs = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Se o arquivo não existir ou não for um JSON válido, cria uma lista vazia
            logs = []

        # Adiciona a nova entrada à lista de logs
        logs.append(log_entry)

        # Salva a lista atualizada de logs de volta ao arquivo
        with open(arquivo_log, "w") as file:
            json.dump(logs, file, indent=2)    


    def login(self):
        
        # Variáveis para armazenar login e senha
        self.login_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        # Carregar informações de login e senha do arquivo JSON
        self.usuarios = self.carregar_usuarios()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)


        # Tela de Boas-vindas
        self.label_welcome = tk.Label(self.login_frame, text="Bem-vindo ao Sistema de Lavagem de Carros!", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        # Entradas para login e senha
        self.label_login = tk.Label(self.login_frame, text="Login:")
        self.entry_login = tk.Entry(self.login_frame, textvariable=self.login_var)

        self.label_senha = tk.Label(self.login_frame, text="Senha:")
        self.entry_senha = tk.Entry(self.login_frame, textvariable=self.senha_var, show="*")

        self.label_login.pack(pady=5)
        self.entry_login.pack(pady=5)
        self.label_senha.pack(pady=5)
        self.entry_senha.pack(pady=5)

        # Botões de Login e Cadastro
        self.button_login = tk.Button(self.login_frame, text="Login", command=self.autenticar_usuario)
        self.button_login.pack(pady=10)

        self.button_cadastrar = tk.Button(self.login_frame, text="Cadastrar", command=self.cadastrar_usuario)
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
                    self.user_type = tipo_usuario
                    self.user_id = id_usuario
                    #self.load_user()
                    self.login_frame.destroy()  # Destruir o frame de login
                    self.abrir_interface()
                    #Gerar log
                    message = str(f'Tipo de usuario: {tipo_usuario} Autenticado com ID: {id_usuario}')
                    self.program_log(message)
                elif tipo_usuario == "funcionario":
                    self.user_type = tipo_usuario
                    self.user_id = id_usuario
                    self.login_frame.destroy()  # Destruir o frame de login
                    self.abrir_interface()
                    #gerar log
                    message = str(f'Tipo de usuario: {tipo_usuario} Autenticado com ID: {id_usuario}')
                    self.program_log(message)
            else:
                messagebox.showerror("Erro de login", "Credenciais inválidas. Tente novamente.")
        else:
            messagebox.showerror("Erro de login", f"Usuário {tipo_usuario} não encontrado.")


    def load_user(self):
        try:
            with open("./pythonCode/cco23_2/POO02/ProjetoFinal/user_info.json", "r") as file:
                user_load = json.load(file)
            
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'usuarios.json' não encontrado.")
            self.root.destroy()
            
        
        iduser = gerar_id()
        #user_load = {}
        for self.user_id, data in user_load.items():
            self.cliente = Cliente(iduser,data["nome"], data["tipo"], data["contato"])
            message = str(f'Dados de usuario: {data["nome"], data["tipo"], data["contato"]} Autenticado com ID: {self.user_id}')
            self.program_log(message)

        return
    

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

    def encerrar_aplicativo(self):
        self.root.destroy()  # Destroi a janela principal, encerrando o aplicativo
    
    # Lógica para abrir a interface de usuario
    def abrir_interface(self):
        #gerar log
        message = str(f"Interface do cliente Aberta ID: {self.user_id}")
        self.program_log(message)

        self.option = tk.IntVar()

        self.interface_frame = tk.Frame(self.root)
        self.interface_frame.pack(padx=20, pady=20)

        self.label_location = tk.Label(self.interface_frame, text="Menu Principal", font=("Helvetica", 20))
        self.label_location.pack(pady=10)

        self.label_welcome = tk.Label(self.interface_frame, text=f"Bem Vindo ao Menu {self.user_type}\n Seu ID é: {self.user_id}", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        self.label_option = tk.Label(self.interface_frame, text=' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n Opção: ', anchor="w")
        self.entry_option = tk.Entry(self.interface_frame, textvariable=self.option)

        self.label_option.pack(pady=5, anchor="w")
        self.entry_option.pack(pady=6)

        self.button_executar = tk.Button(self.interface_frame, text="Executar", command=self.selection_main_menu)
        self.button_executar.pack(pady=10)
       

        self.button_close = tk.Button(self.interface_frame, text="Sair", command=self.encerrar_aplicativo)
        self.button_close.pack(pady=10)

        self.label_result = tk.Label(self.interface_frame, text='', anchor="w")
        self.label_result.pack(pady=10, anchor="w")

        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.rowconfigure(8, weight=1)

    def erase(self):
        # Destruir o botão "Listar OS" quando o botão "Voltar" é acionado
        self.button_listar_os.destroy()

        #gerar log
    def abrir_listas(self):    
        message = str(f"Interface do cliente Aberta ID: {self.user_id}")
        self.program_log(message)

        self.option = tk.IntVar()

        self.interface_frame = tk.Frame(self.root)
        self.interface_frame.pack(padx=20, pady=20)

        self.label_location = tk.Label(self.interface_frame, text="Menu Principal", font=("Helvetica", 20))
        self.label_location.pack(pady=10)

        self.label_welcome = tk.Label(self.interface_frame, text=f"Bem Vindo ao Menu {self.user_type}\n Seu ID é: {self.user_id}", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        self.label_option = tk.Label(self.interface_frame, text=' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n Opção: ', anchor="w")
        self.entry_option = tk.Entry(self.interface_frame, textvariable=self.option)

        self.label_option.pack(pady=5, anchor="w")
        self.entry_option.pack(pady=6)

        self.button_executar = tk.Button(self.interface_frame, text="Executar", command=self.selection_main_menu)
        self.button_executar.pack(pady=10)

        self.button_close = tk.Button(self.interface_frame, text="Sair", command=self.encerrar_aplicativo)
        self.button_close.pack(pady=10)

        self.label_result = tk.Label(self.interface_frame, text='', anchor="w")
        self.label_result.pack(pady=10, anchor="w")

        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.rowconfigure(8, weight=1)
        
    
    
    #menus de Interacao
    def show_main_menu(self):
        #self.button_listar_os.destroy()


        self.program_log(f'Acesso ao Menu Principal\n Seu ID é: {self.user_id}')

        self.label_location.config(text="Menu principal")
        
        self.label_welcome.config(text=f"Menu Usuario\n Seu ID é: {self.user_id}")
        #self.label_welcome.pack(pady=10)

        self.label_option.config(text=' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n Opção: ')
        #self.label_option.pack(pady=5, anchor="w")
        
        self.label_result.config(text=" ")
        
        self.button_executar.config(text='Executar', command = self.selection_main_menu)
        self.button_executar.pack(pady=10)  

        #button actions
    
    def selection_main_menu(self):
        """"Funcao com a logica para selecao do menu principal"""
        ###1 - Ordem de Serviço \n 2 - Veiculo \n 3 - menu03 \n 4 - Menu 04 \n 5 - Menu 05 \n Opção:
        try:
            option_tip = self.option.get()
        except tk.TclError:
            self.label_result.config(text="Entrada inválida. Certifique-se de fornecer os valores corretos.")
            return

        if option_tip == 1: #main menu / 1 - Ordem de Serviço
            self.program_log(f'Acessado Menu principal {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")
            self.show_os_menu() 
            
        elif option_tip == 2: # main menu / 2 - Cadastrar Veiculo
            self.program_log(f'Acessado Menu principal {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")
            self.show_RegisterVehicle_menu
            
        
        elif option_tip == 3: #main menu / 3 - Consultar OS
            self.program_log(f'Acessado Menu principal {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")
            self.show_ConsultOS_menu() 

        elif option_tip == 4: #main menu / 4 - Menu 04
            self.program_log(f'Acessado Menu principal {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")
            

        elif option_tip == 5: #main menu / 5 - Menu 05
            self.program_log(f'Acessado Menu principal {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")
            

        else:
            self.label_result.config(text="Opção Inválida. Insira um valor entre 0 e 5.")        
        
    
    def show_os_menu(self):
        self.program_log('Acessado Menu Ordem de servico')
        self.label_location.config(text="Menu Ordem de Serviço")
        self.label_welcome.config(text="Escolha um das opçoes")
        self.label_option.config(text="1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: ")
        self.label_welcome.pack(pady=10)
        self.label_option.pack(pady=5, anchor="w")
        self.button_executar.config(command=self.selection_os_menu)
        self.button_executar.pack(pady=10)
    
    def selection_os_menu(self):
        try:
            option_tip = self.option.get()
        except tk.TclError:
            self.label_result.config(text="Entrada inválida. Certifique-se de fornecer os valores corretos.")
            return

        if option_tip == 1: # Consultar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao Ordem de servico {option_tip}")
            self.label_welcome.config(text=f" ")
            self.label_option.config(text=f"  {self.oss[0].__str__()}")

            
            #self.button_executar.config(text='Buscar', command=lambda: (self.#visualizar_ordem_servico(oss, option_tip)))
            #self.button_executar.pack(pady=10)

            #self.button_executar.config(text='Voltar', command=lambda: (self.show_main_menu(), self.erase()))
            #self.button_executar.pack(pady=10)

            # Usando lambda para chamar consultar_ordens_servico com o argumento
            self.button_listar_os = tk.Button(self.interface_frame, text="Listar OS", command=lambda: self.consultar_ordens_servico(oss))
            self.button_listar_os.pack(pady=10)

            
            

        elif option_tip == 2:  # Gerar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nGerar nova OS")
            #self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Gerar Ordem de serviço")
            #self.label_option.pack(pady=5, anchor="w")
            
            self.button_executar.config(text='Voltar',command = self.show_main_menu)
            self.button_executar.pack(pady=10)
            

        elif option_tip == 3:  # Adicionar Serviços
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nAdicionar Servicos")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Adicionar servicos a Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 4:  # Cancelar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nCancelar OS")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Cancelar um Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 5:  # Encerrar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nEncerrar OS")
            self.label_welcome.pack(pady=10)
            if self.user_type == 'funcionario':
                self.label_option.config(text="  Encerrar um Ordem de serviço")
                self.label_option.pack(pady=5, anchor="w")
                self.button_executar.config(command = self.show_main_menu)
            else:
                self.label_option.config(text="Procure um funcionario para encerrar a sua ordem")
                self.label_option.pack(pady=5, anchor="w")
            self.button_executar.config(command = self.show_main_menu)
            #self.button_executar.pack(pady=10)

        elif option_tip == 0:  # Encerrar OS
            self.show_main_menu()


        else:
            self.label_result.config(text="Opção Inválida. Insira um valor entre 0 e 5.")  



    #funcoes para apresentacao de tela
    def show_RegisterVehicle_menu(self):
        self.program_log('Acessado Menu Cadastro de veículo')
        self.label_location.config(text="Menu Ordem de Serviço")
        self.label_welcome.config(text="Escolha um das opçoes")
        self.label_option.config(text="1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: ")
        self.label_welcome.pack(pady=10)
        self.label_option.pack(pady=5, anchor="w")
        self.button_executar.config(command=self.selection_os_menu)
        self.button_executar.pack(pady=10)
    
    def selection_RegisterVehicle_menu(self):
        try:
            option_tip = self.option.get()
        except tk.TclError:
            self.label_result.config(text="Entrada inválida. Certifique-se de fornecer os valores corretos.")
            return

        if option_tip == 1: # Consultar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao Ordem de servico {option_tip}")
            self.label_welcome.config(text="Menu Consultar OS")
            #self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Consultar Ordem de serviço")
            #self.label_option.pack(pady=5, anchor="w")
            
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)
            

        elif option_tip == 2:  # Gerar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nGerar nova OS")
            #self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Gerar Ordem de serviço")
            #self.label_option.pack(pady=5, anchor="w")
            
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)
            

        elif option_tip == 3:  # Adicionar Serviços
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nAdicionar Servicos")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Adicionar servicos a Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 4:  # Cancelar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nCancelar OS")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Cancelar um Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 5:  # Encerrar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nEncerrar OS")
            self.label_welcome.pack(pady=10)
            if self.user_type == 'funcionario':
                self.label_option.config(text="  Encerrar um Ordem de serviço")
                self.label_option.pack(pady=5, anchor="w")
                self.button_executar.config(command = self.show_main_menu)
            else:
                self.label_option.config(text="Procure um funcionario para encerrar a sua ordem")
                self.label_option.pack(pady=5, anchor="w")
            self.button_executar.config(command = self.show_main_menu)
            #self.button_executar.pack(pady=10)

        elif option_tip == 0:  # Encerrar OS
            self.show_main_menu()


        else:
            self.label_result.config(text="Opção Inválida. Insira um valor entre 0 e 5.")  
        
    def show_ConsultOS_menu(self):
        self.program_log('Acessado Menu Oredem de servico')
        self.label_location.config(text="Menu Ordem de Serviço")
        self.label_welcome.config(text="Escolha um das opçoes")
        self.label_option.config(text="1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: ")
        self.label_welcome.pack(pady=10)
        self.label_option.pack(pady=5, anchor="w")
        self.button_executar.config(command=self.selection_os_menu)
        self.button_executar.pack(pady=10)
    
    def selection_ConsultOS_menu(self):
        try:
            option_tip = self.option.get()
        except tk.TclError:
            self.label_result.config(text="Entrada inválida. Certifique-se de fornecer os valores corretos.")
            return

        if option_tip == 1: # Consultar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao Ordem de servico {option_tip}")
            self.label_welcome.config(text="Menu Consultar OS")
            #self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Consultar Ordem de serviço")
            #self.label_option.pack(pady=5, anchor="w")
            
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)
            

        elif option_tip == 2:  # Gerar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nGerar nova OS")
            #self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Gerar Ordem de serviço")
            #self.label_option.pack(pady=5, anchor="w")
            
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)
            

        elif option_tip == 3:  # Adicionar Serviços
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nAdicionar Servicos")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Adicionar servicos a Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 4:  # Cancelar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nCancelar OS")
            self.label_welcome.pack(pady=10)
            self.label_option.config(text="  Cancelar um Ordem de serviço")
            self.label_option.pack(pady=5, anchor="w")
            self.interface_frame.destroy()  # Destruir o frame da interface
            self.button_executar.config(command = self.show_main_menu)
            self.button_executar.pack(pady=10)

        elif option_tip == 5:  # Encerrar OS
            self.program_log(f'Acessado Menu Ordem de Servico: Opcao {option_tip}')
            self.label_result.config(text=f"Opcao {option_tip}")

            self.label_welcome.config(text="Menu Ordem de Servico\nEncerrar OS")
            self.label_welcome.pack(pady=10)
            if self.user_type == 'funcionario':
                self.label_option.config(text="  Encerrar um Ordem de serviço")
                self.label_option.pack(pady=5, anchor="w")
                self.button_executar.config(command = self.show_main_menu)
            else:
                self.label_option.config(text="Procure um funcionario para encerrar a sua ordem")
                self.label_option.pack(pady=5, anchor="w")
            self.button_executar.config(command = self.show_main_menu)
            #self.button_executar.pack(pady=10)

        elif option_tip == 0:  # Encerrar OS
            self.show_main_menu()


        else:
            self.label_result.config(text="Opção Inválida. Insira um valor entre 0 e 5.")  
        
   #funcoes para execucao
    def gerar_ordem(self,veiculo,cliente):
        print("  Cadastrar Oredem de serviço")
        oss.appende(OrdemServico(veiculos[veiculo], clientes[self.user_id]))
        oss[4].adicionar_item_servico(servicos[1], 30.0, 10)
        oss[4].calcular_total_ordem()
        return ('****Total da ordem****:', oss[4].calcular_total_ordem)

    def abrir_interface_funcionario(self, id_employer):
         #gerar log
        message = str(f"Interface do cliente Aberta ID: {self.user_id}")
        self.program_log(message)

        self.option = tk.IntVar()

        self.interface_frame = tk.Frame(self.root)
        self.interface_frame.pack(padx=20, pady=20)

        self.label_welcome = tk.Label(self.interface_frame, text="Bem Vindo ao Menu Funcionário\n Seu ID é: 0", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        self.label_option = tk.Label(self.interface_frame, text=' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n Opção: ', anchor="w")
        self.entry_option = tk.Entry(self.interface_frame, textvariable=self.option)

        self.label_option.pack(pady=5, anchor="w")
        self.entry_option.pack(pady=6)

        self.button_executar = tk.Button(self.interface_frame, text="Executar", command=self.selection_main_menu)
        self.button_executar.pack(pady=10)

        self.button_close = tk.Button(self.interface_frame, text="Sair", command=self.encerrar_aplicativo)
        self.button_close.pack(pady=10)

        self.label_result = tk.Label(self.interface_frame, text='', anchor="w")
        self.label_result.pack(pady=10, anchor="w")

        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.rowconfigure(8, weight=1)


        # Configuração para que a coluna e a linha se expandam conforme o tamanho da janela
        self.interface_frame.columnconfigure(0, weight=1)
        self.interface_frame.rowconfigure(8, weight=1)

         # Adiciona um botão "Sair"
        tk.Button(self.interface_frame, text="Sair", command=self.encerrar_aplicativo).grid(row=9, column=0, columnspan=2, pady=10)


    def show_mensage(self):
        messagebox.showinfo("Botão acionado com sucesso")


    def visualizar_ordem_servico(self, oss, numero_os):
        
        # Pesquisar a ordem de serviço pelo número
        ordem_encontrada = None
        for os in oss:
            print(os.numero)
            print(numero_os)
            print(os.numero == str(numero_os))
            if os.numero == str(numero_os):
                
                ordem_encontrada = os
                break

        if ordem_encontrada:
            # Criar uma lista de dicionários para ser usado como entrada para o DataFrame
            data = [ordem_encontrada.to_dict()]

            # Criar uma nova janela Toplevel
            visualizacao_janela = tk.Toplevel()

            # Criar e exibir a interface gráfica dentro da nova janela
            interface = InterfaceTkinter(visualizacao_janela, data)
        else:
            messagebox.showerror("Sem correspondência", "Não foi encontrada uma ordem de serviço com o número fornecido.")



    def consultar_ordens_servico(self, oss):
    # Criar uma lista de dicionários para ser usado como entrada para o DataFrame
        data = []
        for os in oss:
            data.append(os.to_dict())

        # Criar uma nova janela Toplevel
        consulta_janela = tk.Toplevel()

        # Criar e exibir a interface gráfica dentro da nova janela
        interface = InterfaceTkinter(consulta_janela, data)

class InterfaceTkinter:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Visualização de Dados")

        # Criar DataFrame a partir dos dados
        df = pd.DataFrame(data)

        # Criar a tabela com o widget Treeview do ttk
        self.tree = ttk.Treeview(root, columns=list(df.columns), show='headings')

        # Adicionar colunas à tabela
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')  # Ajuste conforme necessário

        # Adicionar dados à tabela
        for index, row in df.iterrows():
            self.tree.insert('', index, values=list(row))

        # Adicionar a tabela à janela
        self.tree.pack(expand=True, fill='both')


def gerar_id():
        numero_aleatorio = str(random.randint(10, 99))
        identificador_unico = str(uuid.uuid4().hex)[:2]  # Dois primeiros dígitos do UUID
        numero_gerado = f"{numero_aleatorio}{identificador_unico}"
        return numero_gerado


if __name__ == "__main__":

    servicos = []
    clientes = []
    veiculos = []
    oss = []
    servicos.append(Servico('Lavação completa', 50.0))
    servicos.append(Servico('Lavação motor', 30.0))
    servicos.append(Servico('Aspiração', 20.0))

    # Criando um cliente
    
    clientes.append(Cliente('0000','Bia', 'Pessoa Física', 'bia@example.com'))
    clientes.append(Cliente('0001','Ana', 'Pessoa Física', 'ana@example.com'))


    # Criando um veículos
    veiculos.append(Veiculo('BCD234', 'ModeloBIaz', 'MarcaBiaCar', 'Pequeno'))

    veiculos.append(Veiculo('ABC123', 'ModeloAnaX', 'MarcaAnaCar', 'Pequeno'))
    veiculos.append(Veiculo('ABC234', 'Modelo123', 'OutraMarcaAnaCar', 'Médio'))

    

    # Associando veículos ao cliente
    clientes[0].setveiculo(veiculos[0])
    
    clientes[1].setveiculo(veiculos[1])
    clientes[1].setveiculo(veiculos[2])


    # Criando ordens de serviço
    oss.append(OrdemServico(veiculos[0], clientes[1]))
    oss[0].adicionar_item_servico(servicos[1], 50.0, 10)
    oss[0].calcular_total_ordem()
    oss[0].fechar_ordem()

    oss.append(OrdemServico(veiculos[2], clientes[0]))
    oss[1].adicionar_item_servico(servicos[2], 30.0, 5)
    oss[1].calcular_total_ordem()
    oss[1].cancelar_ordem()

    oss.append(OrdemServico(veiculos[1], clientes[1]))
    oss[2].adicionar_item_servico(servicos[1], 50.0, 10)
    oss[2].adicionar_item_servico(servicos[2], 30.0, 5)
    oss[2].calcular_total_ordem()

    # Mostrando as ordens de serviço
    #mostrar_ordens_servico([os1, os2, os3])


    import json

# Dados a serem armazenados no JSON
    dados = {
                "cliente": {"cliente1": {"senha": "senha1","id": 1},
                            "cliente2": {"senha": "senha2","id": 2}
                        },
                "funcionario": {"funcionario1": {"senha": "senha3","id": 3},
                                "funcionario2": {"senha": "senha4","id": 4}     
                            }
            }
    #Arquivo  com os dados de login e senha
    # Nome do arquivo JSON
    nome_arquivo = "./pythonCode/cco23_2/POO02/ProjetoFinal/usuarios.json"

    # Escrever os dados no arquivo JSON
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"Arquivo JSON '{nome_arquivo}' gerado com sucesso.")

    # Arquivo com os dados do cliente.
    user_info = {
            1: {"nome": "João da Silva", "tipo": "Pessoa Física", "contato": "joao@example.com"},
            2: {"nome": "Maria Souza", "tipo": "Pessoa Jurídica", "contato": "maria@example.com"}
        }
    # Nome do arquivo JSON
    nome_arquivo = "./pythonCode/cco23_2/POO02/ProjetoFinal/user_info.json"

    # Escrever os dados no arquivo JSON
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(user_info, arquivo, indent=4)

    print(f"Arquivo JSON '{nome_arquivo}' gerado com sucesso.")
 


    root = tk.Tk()
    sistema = SistemaLavagemCarros(root)
    root.mainloop()
