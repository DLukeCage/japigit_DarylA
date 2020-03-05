import pandas as pd
from alpha_vantage.timeseries import TimeSeries

API_KEY = 'E21KPTXMBIYY8TM1'




def getStockdata(symbol):
    try:
        print("Please wait, looking for data\n")
        ts = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = ts.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:
        return "not found"


def main():
    f = open('japi.out', 'w')
    while 1:
        user_input = input("Type the name of the symbol to get the last 1min price or quit to exit\n").upper()
        if user_input != "QUIT":
            response = 'The current price of {} is {}\n'.format(user_input, getStockdata(user_input))
            print(response)
            f.write(response)
        else:
            raise SystemExit


main()
