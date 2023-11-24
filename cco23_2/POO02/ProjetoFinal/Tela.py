import tkinter as tk
from tkinter import ttk
#from main_GUI import verifica_login
from main import *

cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"  # letra / letters
cor5 = 'gray'
cor6 = 'red'
count = 0
command = str()

class SistemaGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Controle")
        self.geometry("800x600")

        # Criação de estilos para ttk
        style = ttk.Style(self)
        style.configure("Verde.TFrame", background="green")  # Defina a cor verde aqui
        style.configure("Branco.TFrame", background="#feffff")  # Defina a cor branco aqui

        # Criação de abas
        self.tabControl = ttk.Notebook(self)

        # Aba de Cliente
        self.cliente_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.cliente_tab, text="Pagina de Login")
        

            #------FRAME 00--------------

        # Frame em grade dentro da aba Cliente
        self.cliente_frame = ttk.Frame(self.cliente_tab, style="Verde.TFrame")
        self.cliente_frame.grid(row=0, column=0, padx=10, pady=10)


            #------FRAME 01--------------

        self.container01 = ttk.Frame(self.cliente_tab, style="Verde.TFrame")
        self.container01.grid(row=1, column=0, padx=10, pady=10)
       
            #------ROW 00--------------

        #instanciando uma mensagem dentro do frame 01
        self.msg11 = tk.Label(self.container01, text='LOGIN')
        self.msg11["font"] = ("Verdana", "20", "italic", "bold")
        self.msg11.grid(row=0, column=0, padx=10, pady=10)


            #------ROW 01--------------

         #instanciando outra mensagem dentro de um Label
        self.msg12 = tk.Label(self.container01, text='Entre com o seu usuario')
        self.msg12.grid(row=1, column=0, padx=10, pady=10)


        #------ROW 02--------------

        # ####Decoracao da tela
        self.linha_01 = tk.Label(self.container01, text= '', width=30, anchor=tk.NW, bg=cor1, fg=cor4 )
        self.linha_01.grid(row=2, column=0, padx=10, pady=10)


        #------FRAME 01--------------

        # CONTAINER 02
        self.container02 = ttk.Frame(self.cliente_tab, style="Branco.TFrame")
        self.container02.grid(row=2, column=0, padx=10, pady=10)

        #------ROW 00--------------
        self.titulo = tk.Label(self.container02, text= 'Dados do usuario: ')
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo["bg"] = cor2
        self.titulo.grid(row=0, column=0, padx=10, pady=10)

        #------ROW 01--------------
        self.stringUsername = tk.StringVar(value='user1')
        self.username = tk.Entry(self.container02, textvariable=self.stringUsername)
        self.username.grid(row=1, column=0, padx=10, pady=10)

        #------ROW 02--------------
        self.stringPassword = tk.StringVar(value="pwd1")
        self.password = tk.Entry(self.container02, textvariable=self.stringPassword, show='*')
        self.password.grid(row=2, column=0, padx=10, pady=10)

        #------ROW 03--------------
        self.submit = tk.Button(self.container02, text='Send')
        self.submit.bind('<Button-1>', lambda event: self.sendForm())
        self.submit.grid(row=3, column=0, padx=10, pady=10)

        #--------Roda pé----------
        # Botão de inicialização
        self.btn_inicializar = tk.Button(self, text="Inicializar Sistema", command=self.inicializar_sistema)
        self.btn_inicializar.pack(side=tk.BOTTOM, pady=10)

        # Botão para encerrar o programa
        self.btn_encerrar = tk.Button(self, text="Encerrar", command=self.destroy)
        self.btn_encerrar.bind('<Button-1>', lambda event: self.mensagem('sair'))
        self.btn_encerrar.pack(side=tk.BOTTOM, pady=10)

        # # Aba de Funcionário
        # self.funcionario_tab = ttk.Frame(self.tabControl)
        # self.tabControl.add(self.funcionario_tab, text="Funcionário")

        # # Frame em grade dentro da aba Funcionário
        # self.funcionario_frame = ttk.Frame(self.funcionario_tab, style="Verde.TFrame")
        # self.funcionario_frame.grid(row=0, column=0, padx=10, pady=10)

        # # Botão de inicialização para Funcionário
        # self.btn_inicializar_funcionario = tk.Button(self.funcionario_frame, text="Inicializar Sistema", command=self.inicializar_sistema)
        # self.btn_inicializar_funcionario.grid(row=0, column=0, pady=10)

        # # Adicione mais widgets organizados em grade conforme necessário...

        # Posicionamento
        self.tabControl.pack(expand=1, fill="both")

    def inicializar_sistema(self):
        print('Inicializar sistema pressionado')
        screen.titulo['text'] = 'Inicializar sistema pressionado'


    def mensagem(self, txt):
        print("=" * 30)
        print(f"{txt}")
        print("=" * 30)
        print()

    def mudarTexto(self):
        global count
        if self.msg11['text'] == 'LOGIN':
            self.msg11['text'] = 'Fui apertado!!!'
            self.msg11['fg'] = cor2
        else:
            self.msg11['text'] = count
            self.msg11['fg'] = cor6
            count += 1

    def sendForm(self):
        self.mensagem('botao Send Form')
        print(f"Username inserido: ", self.stringUsername.get())
        print(f"Password inserida: ", self.stringPassword.get())
        check_login()

    def sendOpt(self):
        self.mensagem('botao Send Option')
        self.sendCommand()
        check_option()

    def sendCommand(self):
        
        self.mensagem('botao Send Command')
        print(f"Username inserido: ", self.stringUsername.get())
        global command
        print(f'Variavel ANTES com valor: {command}') 
        command = self.stringUsername.get()
        print(f'Variavel DEPOIS com valor: {command}')

    
def testVer():
    printing('chamou a funcao!!')        


def check_login():
    a = sistema.autenticar_e_acessar_ambiente(screen.stringUsername.get(), screen.stringPassword.get())
    print(a)
        
    
    if a == 1:               
        if screen.stringUsername.get() == "user1":
            print(f'autenticado como: {screen.stringUsername.get()}')
            screen.tabControl.tab(screen.cliente_tab, text="Cliente")
            menu_user(0)
        elif screen.stringUsername.get() == "user2":
            testVer()
            #menu_user(1)
        elif a == 2:
            print('Menu Funcionario')
            menu_func()
    else:
        screen.msg11['text'] = a

    


def menu_user(client_id):
    print(f'Entrando menu User\nlogando com id: {client_id}')
    printing("    Menu Usuario-tela")
    print(' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05\n 0 para voltar ao meno principal')

    
    
    screen.msg11['text'] = 'Menu Usuario'
    screen.msg12['text'] = f'Bem-vindo ao ambiente do tela\nUsuario id: {client_id}!'
    screen.titulo['text'] = ' 1 - Ordem de Serviço \n 2 - Cadastrar Veiculo \n 3 - Consultar OS \n 4 - Menu 04 \n 5 - Menu 05 \n 0 - #Encerrar \n Opção: '
    screen.password.grid_forget()
    screen.stringUsername.set('')
    screen.submit.bind('<Button-1>', lambda event: screen.sendOpt())

def check_option():
        global command
        print('Acessando funcao verificar opcao')
        print('teste opcao 1')
        print(f'Valor: {command},Tipo: {type(command)}')
        
        if command == '0' or command == 0:
            print('opcao 0 selecionada')
            menu_user()
        if command == '1' or command == 1:
            print('opcao 1 selecionada')
            
            print(command == 1 or command == '1')

            printing("    Menu Ordem de Serviço")
            print(' 1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: ')

            screen.msg11['text'] = 'Menu Usuario\nMenu Ordem de Serviço'
            screen.titulo['text'] = '1 - Consultar OS \n 2 - Gerar OS \n 3 - Adicionar Serviços \n 4 - Cancelar OS \n 5- Encerrar OS \n 0 - volta \n: '
            screen.stringUsername.set('')
            screen.submit.bind('<Button-1>', lambda event: screen.sendCommand())

                    
            
        elif command == '2':
            print('opcao02')
            screen.titulo['text'] = 'Selecionado\n Opcao: 02'
            
                
                
            # menu financeiro         
        elif command == '3':
            print('opcao03')
            screen.titulo['text'] = 'Selecionado\n Opcao: 02'
            
                

        # Menu Administrativo
        elif command == '4':
        
        
            printing('opcao04')
            screen.titulo['text'] = 'Selecionado\n Opcao: 02'
            

        
        elif command == '5':
            screen.titulo['text'] = 'Selecionado\n Opcao: 02'
            print(" Lotação por curso")
            printing('opcao05')
 

        else:
            print('Opção Inválida! Tente novamente...')
            
            screen.stringUsername = tk.StringVar(value='Opção Inválida! Tente novamente...')




if __name__ == "__main__":
    inicializarAutent()
    inicializarSitema()

    screen = SistemaGUI()
    screen.mainloop()

