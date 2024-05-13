import tkinter as tk
from tkinter import ttk, scrolledtext
import chatBotOpenAi


def send_question():
    prompt = user_input.get("1.0", tk.END).strip()

    if prompt:
        response = chatBotOpenAi.chat(prompt)
        chat_history.insert(tk.END, f"\nUsuário: {prompt}\nBot: {response}\n\n")
        user_input.delete("1.0", tk.END)


def create_gui():
    chat_window = tk.Tk()
    chat_window.title("Gemini Chat Bot")
    chat_window.geometry("600x400")

    # Botão para enviar a pergunta
    send_button = ttk.Button(chat_window, text="Enviar", command=send_question)
    send_button.pack(pady=10)

    # Campo de entrada para a pergunta do usuário
    global user_input
    user_input = scrolledtext.ScrolledText(chat_window, height=5, width=50)
    user_input.pack(pady=10)

    # Histórico da conversa
    global chat_history
    chat_history = scrolledtext.ScrolledText(chat_window, height=20, width=50)
    chat_history.pack(pady=10)

    chat_window.mainloop()


if __name__ == "__main__":
    create_gui()
