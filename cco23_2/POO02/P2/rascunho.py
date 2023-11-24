from GoogleNews import GoogleNews
googlenews = GoogleNews()
import pandas as pd

print(googlenews.getVersion())

googlenews.get_news('APPLE')


googlenews=GoogleNews(period='d')
googlenews.setlang('pt')
googlenews.search('petrobras')

result=googlenews.result()
df=pd.DataFrame(result)
df.head()

for i in range(1,5):
    googlenews.getpage(i)
    result=googlenews.result()
    df=pd.DataFrame(result)

googlenews.gettext()

googlenews.get_links()

########
