def t (tickaa, strike1a, strike2a, perda, intervla):
    import numpy as np
    import pandas as pd

    #Data Source
    import yfinance as yf

    #Data viz
    import plotly.graph_objs as go

    pd.options.display.max_rows=9999
    pd.options.display.max_columns=15
    pd.set_option("display.max_columns", 100)
    pd.set_option('display.width', 1000)



    #g='F'
    perd=perda
    intervl=intervla

    # [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

    #g=input("Enter Ticker :")
    g = tickaa
    #perd=input("Enter no of days '5d','2d','1d' :")
    #intervl=input("Enter mins '5m','1m' :")


    #df=pd.DataFrame()
    #Interval required 5 minutes
    data = yf.download(tickaa, period=perd, interval=intervl)

    df=pd.DataFrame(data)
    #print(df.tail(5))
    df.reset_index(drop=False,inplace=True)
    #df.set_index()
    #print(df.shape[0],'   ','\n\n',df.tail(5))

    #print(df.tail(6))


    #dp=pd.DataFrame()
    dp=pd.DataFrame()
    for x in range(df.shape[0]):
        dp=dp.append(df.iloc[x,[0,1,4,6]])

    #    dp[x]=pd.DataFrame([df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000])
        #dp=pd.DataFrame([df.iloc[x,0],df.iloc[x,5]])
    #  print(df.iloc[x,0],df.iloc[x,5],df.iloc[x,6]/1000)
    print('\n\n\n')
    #print(dp)
    dp=pd.DataFrame(dp)
    dp.columns=['n','Price','close','Vol']
    #print(dp)

    d=[] ; m1=[];m2=[];m3=[]
    strike1=int(strike1a)
    strike2=int(strike2a)


    for x in range(dp.shape[0]):
        d.append(g)
        m1.append(strike1)
        m2.append(strike2)

    df4=pd.DataFrame([d,m1,m2])
    #print(df4)

    df4=df4.T


    df4.columns=['Ticker','strike1','strike2']



    df3=pd.concat([df4,dp],axis=1)
    #df3=df3.T

    df3['(from_strike1)']=df3['strike1']-df3['close']
    print(df3.tail(36))



#tick,strike1a,strike2a,perda,intervla
#t ('^NDX',13400,13410,'5d','1d')
#t ('TSLA',627,635,'5d','1d')


#t ('^NDX',13420,13430,'1d','1m')
#t ('^NDX',13400,13410,'1d','60m')
t ('GME',280,290,'1d','5m')   
#t ('MELI',1390,1395,'10d','60m')
#t ('ADSK',300,302.5,'1d','60m')



# [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

     #perd=input("Enter no of days '5d','2d','1d' :")
     #intervl=input("Enter mins '5m','1m' :")
