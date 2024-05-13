#Instalando o SDK do Google
#!pip install -q -U google-generativeai
#pip install IPython
## -q quiet para não mostrar a saida na tela -U update para o caso de já existir atualizar
#To use the userdata module outside of Google Colab, you will need to install the google-auth and google-cloud-secret-manager libraries.
#pip install google-auth google-cloud-secret-manager

#Import the necessary packages.
import pathlib
import textwrap

import google.generativeai as genai
from geminiSetting import *
from IPython.display import display
from IPython.display import Markdown
#from google.colab import userdata # Used to securely store your API key


#Configurações iniciais
generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
#The safety_settings argument lets you configure what the model blocks and allows in both prompts and responses.
safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }
genai.configure(api_key='your_key') #usar API Keys
#Configurando o modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

#Codigo de teste
#response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
#print(response.text)
# #Listando os modelos disponíveis
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

#print function
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#Inicialização do chat
def chatBoot():
    chat = model.start_chat(history=[])

    #prompt = input(display(to_markdown('*Faça uma Pergunta: *')))
    prompt = input(print('Faça uma Pergunta: '))

    while prompt != "fim":
        response = chat.send_message(prompt)
        #display(to_markdown("*Resposta*: "), to_markdown(response.text))
        print("Resposta:", response.text, '\n\n')
        prompt = input('Proxima pergunta: ')
    display("Volte sempre que precisar!!!")

if __name__ == '__main__':
  chatBoot()


