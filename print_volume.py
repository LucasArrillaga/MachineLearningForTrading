import pandas as pd
import matplotlib.pyplot as plot

def test_run():
    df=pd.read_csv("BABA.csv")
    print (df[['Volume','Date']])
    #df[['Close','High']].plot()

    plot.plot(df['Date'].tail(10),df[['Close','High']].tail(10))
    plot.show()

if __name__ == "__main__":
    test_run()
