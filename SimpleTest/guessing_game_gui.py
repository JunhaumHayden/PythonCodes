import tkinter as tk
from tkinter import messagebox
import requests
import random

# Get the list of words from the API.
url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url)
data = resposta.json()

# Initialize the game state.
continuar_jogando = True
valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']
dica = valor_secreto['dica']

# Create the main window.
root = tk.Tk()
root.title("Jogo da Forca")

presentation_label = tk.Label(root, text="Adivinhe a palavra secreta!!\n")
presentation_label.pack()

# Create the label to display the word.
word_label = tk.Label(root, text="_ " * len(valor_secreto['palavra']))
word_label.pack()


# Create the label to display the hint.

hint_label = tk.Label(root, text=valor_secreto['dica'])
hint_label.pack()
cola_label = tk.Label(root, text=valor_secreto['palavra'])
cola_label.pack()

# Create the entry box for the user's guess.
guess_entry = tk.Entry(root)
guess_entry.pack()

# Create the button to submit the guess.
submit_button = tk.Button(root, text="Adivinhar", command=lambda: check_guess())
submit_button.pack()

# Create a variable to track the game state.
flag = True
# Function to start a new game.
def start_game():
    global valor_secreto, palavra_secreta, dica

    # Get a random word from the list.
    valor_secreto = random.choice(data)
    palavra_secreta = valor_secreto['palavra']
    dica = valor_secreto['dica']

    # Update the labels and entry box.
    word_label.configure(text="_ " * len(palavra_secreta))
    hint_label.configure(text=dica)
    cola_label.configure(text=f"cola: {valor_secreto['palavra']}")
    guess_entry.delete(0, tk.END)

# Function to check the user's guess.
def check_guess():
    guess = guess_entry.get()
    if guess == palavra_secreta:
        # The user guessed the word correctly.
        word_label.configure(text=palavra_secreta)
        tk.messagebox.showinfo("Parabéns", "Você ganhou!")

        # Ask the user if they want to continue playing.
        continuar = tk.messagebox.askyesno("Continuar", "Deseja continuar jogando?")
        if continuar:
            start_game()
        else:
            root.destroy()
    else:
        # The user guessed the word incorrectly.
        tk.messagebox.showerror("Erro", "Você errou!")


# Start the main loop.
root.mainloop()











