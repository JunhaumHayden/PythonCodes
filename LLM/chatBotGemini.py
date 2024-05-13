import google.generativeai as genai
import textwrap
from IPython.display import Markdown
from geminiSetting import *

# Configurações iniciais
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

# As configurações de segurança permitem configurar o que o modelo bloqueia e permite em prompts e respostas.
safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}

# Configurando o modelo
#genai.configure(api_key=GOOGLE_API_KEY)
genai.configure(api_key='your_key')
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings,)

def chat(prompt):
    response = model.generate_content(prompt)
    return response.text

#response = model.generate_content("Que empresa criou o modelo de IA Gemini?")
#print(response.text)