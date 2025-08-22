import time

import pyautogui

# Aguarda 2 segundos para o usuário se preparar
time.sleep(2)

# Abre o Spotlight Search no macOS
pyautogui.hotkey("command", "space")
time.sleep(1)

# Digita "TextEdit" para abrir o editor de texto padrão do macOS
pyautogui.write("TextEdit")
time.sleep(1)
pyautogui.press("enter")

# Aguarda o TextEdit abrir
time.sleep(2)

# Se necessário, fecha a janela inicial do TextEdit (onde ele pede para abrir um arquivo)
pyautogui.hotkey("command", "n")  # Cria um novo documento

# Digita um texto automático
pyautogui.write("Olá! Este é um exemplo de RPA com Python.", interval=0.1)

# Salva o arquivo
pyautogui.hotkey("command", "s")
time.sleep(1)

# Define o nome do arquivo
pyautogui.write("meu_rpa.txt")
time.sleep(1)
pyautogui.press("enter")  # Confirma salvar

# Caso seja necessário, confirma a substituição do arquivo
time.sleep(1)
pyautogui.press("enter")
