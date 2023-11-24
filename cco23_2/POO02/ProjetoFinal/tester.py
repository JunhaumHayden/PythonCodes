import tkinter as tk
from tkinter import ttk

cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor4 = "#403d3d"  # letra / letters
cor6 = 'red'

class SistemaGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Controle")
        self.geometry("800x600")

        style = ttk.Style(self)
        style.configure("Verde.TFrame", background="green")
        style.configure("Branco.TFrame", background="#feffff")

        self.tabControl = ttk.Notebook(self)

        self.cliente_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.cliente_tab, text="Pagina de Login")

        self.cliente_frame = ttk.Frame(self.cliente_tab, style="Verde.TFrame")
        self.cliente_frame.grid(row=0, column=0, padx=10, pady=10)

        self.container01 = ttk.Frame(self.cliente_tab, style="Verde.TFrame")
        self.container01.grid(row=1, column=0, padx=10, pady=10)

        self.msg11 = tk.Label(self.container01, text='LOGIN')
        self.msg11["font"] = ("Verdana", "20", "italic", "bold")
        self.msg11.grid(row=0, column=0, padx=10, pady=10)

        self.msg12 = tk.Label(self.container01, text='Entre com o seu usuario')
        self.msg12.grid(row=1, column=0, padx=10, pady=10)

        self.linha_01 = tk.Label(self.container01, text='', width=30, anchor=tk.NW, bg=cor1, fg=cor4)
        self.linha_01.grid(row=2, column=0, padx=10, pady=10)

        self.container02 = ttk.Frame(self.cliente_tab, style="Branco.TFrame")
        self.container02.grid(row=2, column=0, padx=10, pady=10)

        self.titulo = tk.Label(self.container02, text='Dados do usuario: ')
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo["bg"] = cor2
        self.titulo.grid(row=0, column=0, padx=10, pady=10)

        self.stringUsername = tk.StringVar(value='user1')
        self.username = tk.Entry(self.container02, textvariable=self.stringUsername)
        self.username.grid(row=1, column=0, padx=10, pady=10)

        self.stringPassword = tk.StringVar(value="pwd1")
        self.password = tk.Entry(self.container02, textvariable=self.stringPassword, show='*')
        self.password.grid(row=2, column=0, padx=10, pady=10)

        self.submit = tk.Button(self.container02, text='Send', command=self.sendForm)
        self.submit.grid(row=3, column=0, padx=10, pady=10)

        self.btn_inicializar = tk.Button(self, text="Inicializar Sistema", command=self.inicializar_sistema)
        self.btn_inicializar.pack(side=tk.BOTTOM, pady=10)

        self.btn_encerrar = tk.Button(self, text="Encerrar", command=self.destroy)
        self.btn_encerrar.pack(side=tk.BOTTOM, pady=10)

        self.tabControl.pack(expand=1, fill="both")

    def inicializar_sistema(self):
        print('Inicializar sistema pressionado')
        # Lógica de inicialização do sistema aqui

    def mensagem(self, txt):
        print("=" * 30)
        print(f"{txt}")
        print("=" * 30)
        print()

    def sendForm(self):
        self.mensagem('botao Send Form')
        print(f"Username inserido: ", self.stringUsername.get())
        print(f"Password inserida: ", self.stringPassword.get())
        check_login()

def check_login():
    # Lógica de verificação de login aqui
    pass

if __name__ == "__main__":
    screen = SistemaGUI()
    screen.mainloop()
