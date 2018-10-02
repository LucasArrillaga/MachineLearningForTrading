import pandas as pd

def get_max_close(symbol):

    df = pd.read_csv("{}.csv".format(symbol))
    return df['Close'].max()




def test_run():
    for symbol in ['BIDU','BABA']:
        print ("Max close")
        print (symbol, get_max_close(symbol))


if __name__ == "__main__":
    test_run()
