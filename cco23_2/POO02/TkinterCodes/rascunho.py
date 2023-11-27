import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

from GoogleNews import GoogleNews
import pandas as pd
#######
news = GoogleNews()
news.setlang('pt')


data_inicio = '11/11/2022'
data_fim = '11/12/2022'
assunto = 'natacao'
categoria = "noticia"

# Lógica para buscar notícias com base nos filtros (em um dicionário ou lista)
print(data_inicio)
print(data_fim)
print(assunto)

def atualizanoticia(assunto):
    #print(categoria)
    print('printando com Pandas')

    news.search(assunto)
    #result=news.result()
    news.set_time_range(data_inicio,data_fim)

    # Iterar sobre as notícias e adicionar ao widget de texto
    for i in range(1, 2):
        news.getpage(i)
        result = news.result(assunto)
        
        links = news.get_links()
        df = pd.DataFrame(result)

        # Adicionar notícias ao widget de texto
        text_news = df.to_string(index=False, header=False)
        print(tk.END, f"---------PAGE {i}-----------\n{text_news}\n\n*******************************************\n\n")
        print(df)



while True:
    entra = int(input('1 ou 0:'))
    if entra == 1:
        assunto = input('ássunto: ')
        atualizanoticia(assunto)
    else:
        break

# news = GoogleNews()
# news.setlang('pt')

# gools = 'varig'
# news.search(gools)
# result=news.result()
# news.set_time_range('11/11/2023','11/20/2023')
# print('google time')
# print('printando com Pandas')
# for i in range(1,5):
#     news.getpage(i)
#     result=news.result()
#     links = news.get_links()
#     noticia=news.get_news(gools)
#     #print(print)
#     df=pd.DataFrame(result)
#     print(f'PAGE {i}')
#     print(df)

# print(news.getVersion())

# #noticia=news.get_news('apple')
# #print(noticia)




# #news=GoogleNews(period='d')



# #print(result)
# #print('-'*40)

# #df=pd.DataFrame(result)
# #df.head()

# #response = requests.get(f'{API_URL}/{pk}').json()
# # print('printando com Pandas')
# # for i in range(1,5):
# #     news.getpage(i)
# #     result=news.result()
# #     print(print)
# #     df=pd.DataFrame(result)
# #     print(df)

# # text=news.gettext()
# # print('google text')
# # print(text)

# #links = googlenews.get_links()
# #print('google links')
# #print(links)




# ########
