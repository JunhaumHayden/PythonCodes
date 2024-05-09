import tkinter as tk
from gtts import gTTS
from playsound import playsound

# Function to generate and play the audio.
def generate_audio():
    text = text_entry.get()
    language = language_entry.get()

    audio = '/Users/hayden/workspace/pythonCode/SimpleTest/audio.mp3'

    sp = gTTS(text=text, lang=language)
    sp.save(audio)
    playsound(audio)

# Create the main window.
root = tk.Tk()
root.title("Gerador de Áudio")

# Create the label for the text entry.
presentation_label = tk.Label(root, text="Digite um texto para converter em audio:")
presentation_label.pack()
text_label = tk.Label(root, text="Digite o texto:")
text_label.pack()

# Create the entry box for the text.
text_entry = tk.Entry(root)
text_entry.pack()

# Create the label for the language entry.
language_label = tk.Label(root, text="Digite o idioma(pt-br): ")
language_label.pack()

# Create the entry box for the language.
language_entry = tk.Entry(root)
language_entry.pack()

# Create the button to generate the audio.
generate_button = tk.Button(root, text="Gerar Áudio", command=generate_audio)
generate_button.pack()

# Start the main loop.
root.mainloop()