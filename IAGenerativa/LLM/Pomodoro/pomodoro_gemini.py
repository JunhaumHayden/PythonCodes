#Os tempos estão em um formato para que seja possível testar rapidamento o codigo
#Necessário descomentar os parametros para ficar no tempo correto
import threading
import time
import textwrap
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai
#from google.colab import userdata # Para Colab - Usado para guardar a API key em segurança
from geminiSetting import * # Usado para guardar a API key em segurança

#Configurações iniciais - Google Colab
# GOOGLE_API_KEY=userdata.get('secretName')#Acessar a API keys
# genai.configure(api_key=GOOGLE_API_KEY) #usar API Keys
# generation_config = {
#   "candidate_count": 1,
#   "temperature": 0.5,
# }
# #The safety_settings argument lets you configure what the model blocks and allows in both prompts and responses.
# safety_settings={
#     'HATE': 'BLOCK_NONE',
#     'HARASSMENT': 'BLOCK_NONE',
#     'SEXUAL' : 'BLOCK_NONE',
#     'DANGEROUS' : 'BLOCK_NONE'
#     }
#GOOGLE_API_KEY=userdata.get('your_key')#Acessar a API keys


#Configurações iniciais
genai.configure(api_key=GOOGLE_API_KEY) #usar API Keys

# Set parametros de tempo// apague o valor e descomente para os tempos reais
timePomodoro = 30 #25 * 60  # 25 minutes in seconds
pomodoro_time = timePomodoro
short_break_time = 10 #5 * 60  # 5 minutes in seconds
last_short_break_reminder = time.time()
long_break_time = 30 #15 * 60  # 15 minutes in seconds
exercise_time = 5 #10 * 60  # 10 minutes in seconds

# Set lembrete de água
water_reminder_interval = 45 #* 60  # 30 minutes in seconds
last_water_reminder = time.time()

# Set o contador Pomodoro
pomodoro_counter = 0

#Configurando o modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=GENERATION_CONFIG,
                                  safety_settings=SAFETY_SETTING,)

#Funcao auxiliar para exibicao amigavel
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  
#funcao para inicialização do chat
def chatBot():
  chat = model.start_chat(history=[])
  prompt = input(display(to_markdown('*Faça uma Pergunta: *')))
  while prompt != "fim":
    response = chat.send_message(prompt)
    display(to_markdown("*Resposta*: "), to_markdown(response.text))
    #print("Resposta:", response.text, '\n\n')
    prompt = input('Proxima pergunta: ')
  display(to_markdown("**Volte sempre que precisar!!!**"))
  return

#Funcao para dar uma dica
def dicaGemini(dica):
  response = model.generate_content(dica)
  response.text
  display(to_markdown("*Você sabia*: "), to_markdown(response.text))
  return

def decrement_timer():
  global pomodoro_time
  while pomodoro_time > 0:
      time.sleep(1)
      pomodoro_time -= 1
  return False

#Funcao para reiniciar a contagem
def reiniciaTempo():
  global pomodoro_time
  pomodoro_time = timePomodoro
  display(to_markdown('## Hora de se concentrar por 25 min'))
  global timer_thread 
  timer_thread = threading.Thread(target=decrement_timer)
  timer_thread.start()
  return

def tempoPomodoro():
    # Print the remaining time
    print('-'*20)
    print(f"Pomodoro: {pomodoro_time // 60:02d}:{pomodoro_time % 60:02d}")
    print('-'* 20)
    print('\n')
    return

# Start the timer in a separate thread
timer_thread = threading.Thread(target=decrement_timer)
timer_thread.start()

# Main loop
dicaGemini('uma nova dica motivacional sobre rotinas de estudos e finalize com uma frase motivacional')
flag = True
pomodoro_counter = 0
reiniciaTempo()
while flag:
    #tempoPomodoro()
    # Check for water reminder
    if time.time() - last_water_reminder >= water_reminder_interval:
      tempoPomodoro()
      #print("Já bebeu água?")
      display(to_markdown("# Beba água!!!"))
      dicaGemini('uma nova dica curta sobre beber água regularmente')
      #playsound.playsound('water.mp3')  # Play a sound to remind you to drink water
      last_water_reminder = time.time()
      

    if decrement_timer() == False:
          # Long break
          print(pomodoro_counter >1 and pomodoro_counter % 3 == 0)
          if pomodoro_counter >1 and pomodoro_counter % 3 == 0:
            tempoPomodoro()
            #print("tempo para uma parada longa!")
            display(to_markdown("## tempo para uma parada longa!"))
            dicaGemini('uma dica curta sobre paradas longas durante o estudo')
            #playsound.playsound('long_break.mp3')  # Play a sound to indicate the start of a long break
            time.sleep(long_break_time)
            # Exercise reminder
            #print("Fique de pe, vá dar uma volta!")
            display(to_markdown("**Fique de pe, vá dar uma volta!**"))
            dicaGemini('me fale sobre a importancia de dar pausas para fazer exercicios durante a rotina de estudos e me dê dicas de exercicios')
            #playsound.playsound('exercise.mp3')  # Play a sound to remind you to exercise
            time.sleep(exercise_time)
            

          # Short break
          else:
            tempoPomodoro() 
            #print("Tempo para uma parada curta!")
            display(to_markdown("## Tempo para a parada curta numero: "), to_markdown(str(pomodoro_counter + 1)))
            dicaGemini('uma dica sobre paradas curtas durante estudo')
            #playsound.playsound('break.mp3')  # Play a sound to indicate the start of a short break
            time.sleep(short_break_time)
            last_short_break_reminder = time.time()
            # Pomodoro counter
            pomodoro_counter += 1

          
     # Check for user input
    user_input = input("Digite: \n  's' para parar o programa\n  'p' para pause\n  'd' para tirar uma duvida\n  'c' para continar: \n")
    if user_input == "s":
        dicaGemini('um novo exemplo de frase de despedida')
        flag = False
        break
    elif user_input == "p":
        tempoPomodoro()
        input("digite qualquer tecla para continuar...")
        dicaGemini('uma piada sobre estudar')
    elif user_input == "d":
        chatBot()
    elif user_input == "c":
        dicaGemini('uma frase motivacional e divertida para continuar os estudos')
        reiniciaTempo()
        continue  

    