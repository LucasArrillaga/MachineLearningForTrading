import pandas as pd
import matplotlib.pyplot as plot

def test_run():

    #Se define un rango de fechas
    start_date='2010-01-01'
    end_date='2010-12-31'
    dates=pd.date_range(start_date,end_date)

    #Se crea un dataframe con indice Fecha (dates)
    df1=pd.DataFrame(index=dates)
    #print(df1)


    #Se introduce datos de SPY en un dataframe temporal
    dfSPY = pd.read_csv("SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])

    #Se unen los dos dataframes usando DataFrame.join() - usando how='inner' quedan solo los valores que tienen en comun los dataframes
    df1=df1.join(dfSPY,how='inner')

    #Se borran los valores del campo na_values
    #df1=df1.dropna()

    #Leer otros Stocks
    symbols = ['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("{}.csv".format(symbol),index_col='Date',parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1=df1.join(df_temp)

    print (df1)
    #plot.plot(df1)
    #plot.show()





if __name__ == "__main__":
    test_run()
