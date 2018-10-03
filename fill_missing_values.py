"""Fill missing values"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    ##########################################################
    pass  # TODO: Your code here (DO NOT modify anything else)
    ##########################################################
    df_data.fillna(method="ffill",inplace=True)
    df_data.fillna(method="bfill",inplace=True)
    return df_data


def symbol_to_path(symbol, base_dir=""):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df_final = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path, parse_dates=True, index_col="Date",
            usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df_final = df_final.join(df_temp)
        if symbol == "SPY":  # drop dates SPY did not trade
            df_final = df_final.dropna(subset=["SPY"])

    return df_final


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title="Stock", fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()



def test_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2018-10-02')  # one month only
    symbols = ['SPY','TWTR','FB']
    df = get_data(symbols, dates)
    plot_data(df)
    df = fill_missing_values(df)
    plot_data (df)



if __name__ == "__main__":
    test_run()
