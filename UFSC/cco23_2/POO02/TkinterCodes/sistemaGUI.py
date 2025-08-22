import tkinter as tk
from tkinter import *
from tkinter import ttk
from class_Autentica import Sistema
from class_sistema import *
from main import *

#from class_sistema import Cliente
#from class_sistema import OrdemServico
#from class_sistema import Servico

#cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters


import tkinter as tk
from tkinter import ttk

class SistemaGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Controle")
        self.geometry("800x600")
        

        # Criação de estilos para ttk
        style = ttk.Style(self)
        style.configure("Verde.TFrame", background="green")  # Defina a cor verde aqui

        # Criação de abas
        self.tabControl = ttk.Notebook(self)

        # Aba de Cliente
        self.cliente_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.cliente_tab, text="Cliente")

   



        # # Frame em grade dentro da aba Cliente

        self.container01 = tk.Frame(self.cliente_tab, relief='flat')
        self.container01['bg'] = co1
        self.container01['pady'] = 100
        self.container01['padx'] = 100
        self.container01.pack()

          #instanciando um botao
        self.clickme = Button(self.container01)
        self.clickme["text"] = "Click Me"
        self.clickme["font"] = ("Calibri", "10")
        self.clickme["width"] = 10
        self.clickme.bind('<Button-1>', self.mudarTexto)
        self.clickme.pack ()

    #      #     #instanciando um botao
    #     self.sair = tk.Button(self.container01)
    #     self.sair["text"] = "Sair"
    #     self.sair["font"] = ("Calibri", "25")
    #     self.sair["width"] = 15
    #     self.sair.bind('<Button-1>', self.tester)
    #     self.sair.grid()

    def tester(self, event):
        pass
        self.tabControl['text'] = "MUDOU!!"

         #instanciando uma mensagem dentro de um container
        self.msg = Label(self.container01, text= "Label01", bg=co1, fg=co4)
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack (side=TOP)

         #instanciando outra mensagem noframe 01(container01)
        self.msg02 = Label(self.container01, text='Mensagem 02 da caixa 01', bg=co1, fg=co4)
        self.msg02.pack()
        

        # self.container02 = Frame(self.cliente_tab, width=310, height=50, bg= co2, relief='flat')
        # self.container02["pady"] = 20
        # self.container02.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)

        # #Caixas de entrada p/ interacao usuario
        # self.stringEmail = StringVar(value='Email')
        # self.email = Entry(self.container02, textvariable=self.stringEmail)
        # self.email.pack()

        # self.stringUsername = StringVar(value='Username')
        # self.username = Entry(self.container02, textvariable=self.stringUsername)
        # self.username.pack(pady=15, side=TOP)

        # self.stringPassword = StringVar(value="********")
        # self.password = Entry(self.container02, textvariable=self.stringPassword, show='*')
        # self.password.pack(pady=15, side=TOP)

        # self.clickme = Button(self.container02)
        # self.clickme["text"] = "Click Me"
        # self.clickme["font"] = ("Calibri", "20")
        # self.clickme["width"] = 10
        # self.clickme["bg"]=co2
        # self.clickme.bind('<Button-1>', self.mudarTexto)
        # self.clickme.pack ()




        # self.container03 = Frame(self.cliente_tab, width=310, height=50, bg= co2, relief='flat')
        # self.container03["pady"] = 20
        # self.container03.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)

        # self.container04 = Frame(self.cliente_tab, width=310, height=50, bg= co2, relief='flat')
        # self.container04["pady"] = 20
        # self.container04.grid(row=3, column=0, padx=10, pady=10, sticky=NSEW)
        
        
       

        # self.titulo = Label(self.container02, text= 'Dados do usuario: ')
        # self.titulo["font"] = ("Arial", "15", "bold")
        # self.titulo["bg"] = co2
        # self.titulo.pack(side=TOP)

        # ####Decoracao da tela
        # #self.linha_01 = Label(self.container02, text= '', width=275, #height=1, anchor=NW, bg=co1, fg=co4 )
        # #self.titulo["width"] = ("Arial", "10", "bold")
        # #self.linha_01.place(x=20, y=45)
        # #self.linha_01.pack()

        

        
        
        # #instanciando um botao
        # self.sair = Button(self.container03)
        # self.sair["text"] = "Sair"
        # self.sair["font"] = ("Calibri", "25")
        # self.sair["width"] = 15
        # self.sair.bind('<Button-1>', self.clickout)
        # self.sair["command"] =  self.container03.quit
        # self.sair.pack ()


        # #instanciando uma mensagem dentro de um container
        # self.msg = Label(self.container04, text= "Label04", bg=co1, fg=co4)
        # self.msg["font"] = ("Verdana", "20", "italic", "bold")
        # self.msg.pack (side=TOP)

        # # Botão de inicialização
        # self.btn_inicializar = Button(self.container04, text="Inicializar Sistema", command=self.inicializar_sistema)
        # self.btn_inicializar.pack() #grid(row=0, column=0, pady=10)

        # Adicione mais widgets organizados em grade conforme necessário...

        # Aba de Funcionário
        #self.funcionario_tab = ttk.Frame(self.tabControl)
        #self.tabControl.add(self.funcionario_tab, text="Funcionário")

        # Frame em grade dentro da aba Funcionário
       # self.funcionario_frame = ttk.Frame(self.funcionario_tab, style="Verde.TFrame")
        #self.funcionario_frame.grid(row=0, column=0, padx=10, pady=10)

        # Botão de inicialização para Funcionário
       # self.btn_inicializar_funcionario = tk.Button(self.funcionario_frame, text="Inicializar Sistema", command=self.inicializar_sistema)
        #self.btn_inicializar_funcionario.grid(row=0, column=0, pady=10)

        # Adicione mais widgets organizados em grade conforme necessário...

        # Posicionamento
        self.tabControl.pack(expand=1, fill="both")

    
    def clickout(self,event):
        
        print(self.sair["text"], "Foi apertado")
        print("Encerrando Programa!!!\n")

        

    def mudarTexto(self, event):
        count = 2
        print(self.msg['text'])
        if self.msg['text'] == 'Label01':
        
            self.msg['text'] = 'Fui apertado!!!'
        else:
            self.msg['text'] = 'Mais uma vez, já fui apertado:'
            count += 1
            print("O botão foi clicado!")
            print("Email inserido:", self.stringEmail.get())
            print("Username inserido:", self.username.get())
            print("Password inserida:", self.password.get())
            print("\n")
            
                    #     a = sistema.autenticar_e_acessar_ambiente(self.username.get(), self.password.get())
                    
                    #     if a == 1:               
                    #         if self.username.get() == "user1":
                    #             self.msg02['text'] = 'Bem-vindo ao ambiente do app!'
                    #             menu_usuario(0)
                    #         elif self.username.get() == "user2":
                    #             menu_usuario(1)
                    #     elif a == 2:
                    #         print('Menu Funcionario')
                    #         menu_func()
                    # else:
                    #     self.msg['text'] = 'Mensagem 01 Caixa 01'

        


    def inicializar_sistema(self, event):
        self.msg['text'] = 'Inicializar foi apertado'
        # while True:
        #     print('-'*30)
        #     print("Para Usuario: user1, password1")
        #     print("Para Funcionario: employee1, password3")
        #     print('-'*30)
        #     print("\nUsuário 1:")
        #     user=input("Login: ")
        #     password=input("Senha: ")
        #     a = sistema.autenticar_e_acessar_ambiente(user, password)
        
        #     if a == 1:
        #         if user == "user1":
        #             menu_usuario(0)
        #         elif user == "user2":
        #             menu_usuario(1)
        #     elif a == 2:
        #         menu_func()
        #     flag = input("Deseja continuar? ? (s ou n)").lower()
        #     if flag == 'n':

        #         #print("if")
        #         break
        #     else:
        #         #print("else")
        #         continue

         

if __name__ == "__main__":
    #inicializarAutent()
    #inicializarSitema()
    app = SistemaGUI()
    app.mainloop()
