"""Compute mean volume"""

import pandas as pd

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()
    # TODO: Compute and return the mean volume for this stock


def test_run():
    """Function called by Test Run."""
    for symbol in ['BABA', 'BIDU']:
        print ("Mean Volume")
        print (symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    test_run()
