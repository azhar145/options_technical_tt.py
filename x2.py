from yahoo_fin import options 
import pandas as pd
from yahoo_fin import stock_info as f
import textwrap 
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib
matplotlib.use ('Agg')
#show(block=True)


pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
#pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width',15)
#pd.set_option('display.max_colwidth', -1)
tick='F'
tick=input("Enter ticker: ")
df=pd.DataFrame(f.get_data(tick,start_date ='5/5/2021',end_date='6/6/2021',index_as_date = True,interval = "1d"))
df['volume']=df['volume']/1000000
df['open']=df['open'].round(0)
df['adjclose']=df['adjclose'].round(0)
df['close']=df['close'].round(0)
df['low']=df['low'].round(0)
df['high']=df['high'].round(0)
df['volume_p']=df['volume'].shift(1)
df['price_delta']=df['close']-df['close'].shift(1)
df['volume_delta']=df['volume']-df['volume'].shift(1)
print(df)
df['close'].plot()
plt.show()
#print(help(f))
plt.show(block=True)
plt.interactive(False)
