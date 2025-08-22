
from tkinter import *

def enviarFormulario():
    email_inserido = stringEmail.get()
    username_inserido = stringUsername.get()
    password_inserida = stringPassword.get()
    print("O botão foi clicado!")
    print("Email inserido:", email_inserido)
    print("Username inserido:", username_inserido)
    print("Password inserida:", password_inserida)
    mudarTexto()

def mudarTexto():
        if submit['text'] == 'Click Me':
            submit['text'] = 'Fui apertado!!!'
        else:
            submit['text'] = 'Primeiro widget'

janelaPrincipal = Tk()

stringEmail = StringVar(value='Email')
email = Entry(janelaPrincipal, textvariable=stringEmail)
email.pack(pady=15, side=TOP)

stringUsername = StringVar(value='Username')
username = Entry(janelaPrincipal, textvariable=stringUsername)
username.pack(pady=15, side=TOP)

stringPassword = StringVar(value="********")
password = Entry(janelaPrincipal, textvariable=stringPassword, show='*')
password.pack(pady=15, side=TOP)

submit = Button(janelaPrincipal, text='Click Me', command=enviarFormulario)
#submit.bind('<Button-1>', mudarTexto())
submit.pack(pady=15, side=TOP)

janelaPrincipal.mainloop()
