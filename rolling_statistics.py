
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
    symbols = ['SPY']

    # Get stock data
    df = get_data(symbols, dates)

    ax = df['SPY'].plot(title="SPY Media Movil",label='SPY')

    rm_GOOG = df['SPY'].rolling(20).mean()
    rm_GOOG.plot(label='Media Movil',ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()




    #plot_data(df)


def plot_data(df,title="Stock prices"):
    ax = df.plot(title=title,fontsize=9)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

if __name__ == "__main__":
    test_run()
