"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt



def symbol_to_path(symbol, base_dir=""):
    #basedir = ruta
    #symbol = String de simbolo
    """Retorna ruta de archivo CSV de symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp=pd.read_csv(symbol_to_path(symbol),index_col='Date',parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df=df.join(df_temp)
        if symbol== 'SPY':
            df = df.dropna(subset=["SPY"])

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
    #print (df)

    plot_data(df)


    #print (df.ix['2010-01-01':'2010-01-31']) - Imprimir rango de fechas
    #print df['GOOG'] - Imprimir una columna
    #print df[['IBM','GLD']] - Imprimir 2 columnas

    #print (df.ix['2010-03-05':'2010-03-25',['SPY','IBM']])

def plot_data(df,title="Stock prices"):
    ax = df.plot(title=title,fontsize=9)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

if __name__ == "__main__":
    test_run()
