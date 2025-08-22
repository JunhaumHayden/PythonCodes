import requests
import json

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()

# print(data)


print('\n\n\nsymbol search\n\n\n')

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
print('\n\n\nprint for\n\n\n')
for k, v in data.items():
            print(len(v))
            for l in range(len(v)):
                print(v[l],'\n\n')
                for ch, it in v[l].items():
                    print('Nome: {} \nTelefone: {}\n'.format(ch,it))
