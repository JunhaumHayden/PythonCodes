import google.generativeai as genai
import textwrap
from IPython.display import Markdown
from geminiSetting import *

# Configurando o modelo
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=GENERATION_CONFIG,
                              safety_settings=SAFETY_SETTING,)# As configurações de segurança permitem configurar o que o modelo bloqueia e permite em prompts e respostas.

def chat(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    response = chat("Que empresa criou o modelo de IA Gemini?")
    print(response)