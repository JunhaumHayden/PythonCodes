from tkinter import *
import tkinter as tk
from tkinter import ttk
from class_Autentica import Sistema
from class_sistema import *
from main import *


#cores -----------------------------
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters
cor5 = 'gray'
cor6 = 'red'
count = 0


class SistemaGUI:
    def __init__(self, master=None):


        self.fontepadrao = ("Arial", "10")
        #instanciando um container
        self.container01 = Frame(master)
        self.container01["pady"] = 20
        self.container01.pack()
       
        #instanciando uma mensagem dentro de um container
        self.msg = Label(self.container01, text='LOGIN')
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack (side=TOP)

         #instanciando outra mensagem dentro de um pack
        self.msg02 = Label(self.container01, text='Entre com o seu usuario')
        self.msg02.pack()

        # ####Decoracao da tela
        self.linha_01 = Label(self.container01, text= '', width=30, anchor=NW, bg=cor1, fg=cor4 )
        self.linha_01.place(x=20, y=45)
        self.linha_01.pack()

############CONTAINER 02 #############################
        self.container02 = Frame(master, width=30)
        self.container02['bg'] = cor2
        self.container02["pady"] = 20
        self.container02.pack()

        self.titulo = Label(self.container02, text= 'Dados do usuario: ')
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo["bg"] = cor2
        self.titulo.pack(side=TOP)

        self.stringUsername = StringVar(value='Username')
        self.username = Entry(self.container02, textvariable=self.stringUsername)
        self.username.pack(pady=15, side=TOP)

        self.stringPassword = StringVar(value="********")
        self.password = Entry(self.container02, textvariable=self.stringPassword, show='*')
        self.password.pack(pady=15, side=TOP)

        self.submit = Button(self.container02, text='Send')
        self.submit.bind('<Button-1>', lambda event: self.sendForm())
        self.submit.pack(pady=15, side=BOTTOM)







        # self.container03 = Frame(master)
        # self.container03["pady"] = 20
        # self.container03.pack()

        # self.container04 = Frame(master)
        # self.container04["pady"] = 20
        # self.container04.pack()
        
        
       
        # self.titulo = Label(self.container01, text= 'Dados do usuario: ')
        # self.titulo["font"] = ("Arial", "10", "bold")
        # self.titulo.pack()

       

        #instanciando um botao
        self.clickme = Button(self.container01)
        self.clickme["text"] = "Click Me"
        self.clickme["font"] = ("Calibri", "15")
        self.clickme["width"] = 20
        self.clickme['height'] = 3
        self.clickme.bind('<Button-1>', lambda event: self.mensagem('mudar texto'))
        self.clickme['command'] = self.mudarTexto
        self.clickme.pack ()


        #instanciando um botao
        self.sair = Button(self.container01)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "25")
        self.sair["width"] = 15
        self.sair["relief"] ='raised'
        self.sair.bind('<Button-1>', lambda event: self.mensagem('sair'))
        self.sair["command"] = self.container01.quit
        self.sair.pack ()


    def mensagem(self, txt):
        print("="*30)
        print(f"{txt}")
        print("="*30)
        print( )
       

    def mudarTexto(self):
        global count
        if self.msg['text'] == 'LOGIN':
            self.msg['text'] = 'Fui apertado!!!'
            self.msg['fg'] = cor2
        else:
            self.msg['text'] = count
            self.msg['fg'] = cor6
            count +=1

    def sendForm(self):
        print("O botão foi clicado!")
        print(f"Username inserido: ", self.stringUsername.get())
        print(f"Password inserida: ", self.stringPassword.get())
        self.mensagem('botao Send Form')
    
            #return self.stringUsername.get(), self.stringPassword.get()


if __name__ == "__main__":
    
    app = Tk()
    SistemaGUI(app)


    app.title("Sistema de Controle")
    app.geometry("800x600")

    #Passando uma cor de fundo p/ janela
    #cor1='#242323' #cor preta usar website colour picker para pegar codigo da cor

    app.config(bg=cor5)

    #para passar um icone para a janela do programa
    app.iconphoto(False, PhotoImage(file='/Users/hayden/workspace/pythonCode/cco23_2/POO02/TkinterCodes/icons/icon.png') )

    #Para configurar o tamanho da janela
    app.resizable()

    app.mainloop()

